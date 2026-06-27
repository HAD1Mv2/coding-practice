- [Python Intermediate](#python-intermediate)
  - [Parallel Programming using Python](#parallel-programming-using-python)
    - [Multithreading](#multithreading)
      - [Queue](#queue)
      - [Race condition](#race-condition)
        - [How a Race Condition Happens](#how-a-race-condition-happens)
        - [Critical Sections and Race Conditions](#critical-sections-and-race-conditions)
        - [How to Prevent Race Conditions](#how-to-prevent-race-conditions)
        - [Common Symptoms of Race Conditions](#common-symptoms-of-race-conditions)
      - [GIL](#gil)
    - [Multiprocess](#multiprocess)
      - [`if __name__ == '__main__':` guard in Python multiprocessing](#if-__name__--__main__-guard-in-python-multiprocessing)
        - [The Core Problem: Process Spawning](#the-core-problem-process-spawning)
        - [What Happens Without the Guard](#what-happens-without-the-guard)
        - [How the Guard Fixes It](#how-the-guard-fixes-it)
        - [Visualizing the Execution Flow](#visualizing-the-execution-flow)
      - [Pool.apply()](#poolapply)
        - [Key Characteristics](#key-characteristics)
        - [Code Example](#code-example)
        - [When to Use It](#when-to-use-it)
        - [Alternatives for True Parallelism](#alternatives-for-true-parallelism)
  - [Context Manager](#context-manager)
    - [Why Use Context Managers](#why-use-context-managers)
    - [Common Built-In Examples](#common-built-in-examples)
    - [How to Create Custom Context Managers](#how-to-create-custom-context-managers)
      - [1. The Class-Based Approach](#1-the-class-based-approach)
      - [2. The Generator-Based Approach (contextmanager decorator)](#2-the-generator-based-approach-contextmanager-decorator)
  - [Python Error Handling](#python-error-handling)



# Python Intermediate

## Parallel Programming using Python

### Multithreading
Threads: An entity within a process that can be scheduled (also known as "lightweight process").
A process spawn multiple threads.

Pros:
+ All threads within a process share the same memory
+ Lightweight
+ Starting a thread is faster than starting a process
+ Great for I/O bound task
  
Cons:
- Threading is limited by GIL: only one thread running at a time within a process.
- No effect for CPU-bound tasks.
- Not interuptable/killable.
- Careful with race condition.

#### Queue

Queue are linear data structure that follows FIFO (First In Frist Out) principle.

Queue are excelent for thread safe and process safe data exchange and data processing in multithreaded and multiprocessing enviroment.

#### Race condition

A **race condition** occurs when two or more threads access shared data simultaneously, and the final outcome depends on the unpredictable timing or order of their execution. It happens when at least one thread modifies the data while another reads or writes it, leading to data corruption and bugs.

##### How a Race Condition Happens

Imagine two threads trying to increment a shared counter variable with a starting value of 5. The operation counter++ looks like one action, but the CPU actually executes it in three separate steps:

   1. Read: The thread reads the current value from memory (e.g., 5).
   2. Modify: The thread adds 1 to the value in its CPU register (e.g., 5 + 1 = 6).
   3. Write: The thread writes the new value back to memory (e.g., 6). 
   
If the threads overlap, the following race condition occurs:

| Thread 1 (T1)         |Thread 2 (T2)            |Shared Counter Value |
|-----------------------|-------------------------|---------------------|
|1. Reads counter (5).  |     .                   |          5          |
|.                      | 2. Reads counter (5)    |          5          |
|3. Increments to 6     | .                       |          5          |
|4. Writes 6 to memory  | .                       |          6          |
|.                      | 5. Increments to 6      |          6          |
|.                      | 6. Writes 6 to memory   |          6          |

The Result: The counter was incremented twice, but the final value is 6 instead of 7. One update was completely lost. 

------------------------------
##### Critical Sections and Race Conditions

* Critical Section: The specific block of code that accesses the shared, mutable resource (like the counter increment code above).
* Trigger: A race condition occurs when multiple threads execute a critical section at the same time without proper coordination. 

------------------------------
##### How to Prevent Race Conditions
To stop race conditions, you must enforce mutual exclusion, ensuring only one thread can access the critical section at a time.  

* Mutex / Locks: A thread locks the critical section before entering and unlocks it when finished. Other threads must wait until it is unlocked. 
* Atomic Operations: Uses specialized hardware instructions (like Compare-And-Swap) to perform the read-modify-write action as a single, uninterrupted step. 
* Thread-Safe Data Structures: Built-in language collections (like Java's ConcurrentHashMap or C++'s std::atomic) that handle synchronization automatically. 
* Immutability: Designing data to be read-only so multiple threads can access it safely without locks. 

------------------------------
##### Common Symptoms of Race Conditions

* Intermittent Bugs: Code works perfectly during small tests but fails randomly under heavy system load.
* Heisenbugs: Hard-to-reproduce errors that mysteriously disappear when you attach a debugger or add logging statements (because logging alters the thread timing).
* Inconsistent State: Database records or memory objects showing impossible or mismatched data combinations. 

#### GIL

GIL (Global Interpreter Lock)

- A lock that allow only on thread running at a time
- Needed in CPython because memory management is not thread safe
-  How to Avoid GIL:
   -  Use multiprocessing.
   -  Use a different, free threaded python implementation (e.g. Jython, IronPython).
   -  Use Python as a wrapper for third party libraries (C/C++) -> numpy, scipy.
  

### Multiprocess

Process: An instance of a program (e.r python interpreter)

Pros:
+ Takes advantage of multiple cpu and cores.
+ Separate memory space -> memory is not shared between process.
+ Great for CPU bound processing.
+ Processes are independent between each other.
+ Processes are interuptable/killable.
+ One GIl (Global interpreter lock) for each process -> avoids GIL Limitation. 

Cons:
- Heavyweight.
- Starting a process is slower than starting a thread.
- More memory.
- IPC (interprocess of communication) is more complicated.

#### `if __name__ == '__main__':` guard in Python multiprocessing

The `if __name__ == '__main__':` guard is necessary in Python multiprocessing to prevent infinite loops of subprocess creation when using operating systems that start new processes from scratch (like Windows and macOS). 

##### The Core Problem: Process Spawning
When you start a new process in Python, the operating system needs to prepare a fresh Python environment. Depending on your OS, it uses one of two main methods:

* Fork (Linux/Unix): Copies the existing process exactly as it is in memory. It does not need to re-run your script from the top.
* Spawn (Windows, macOS): Starts a brand-new, empty Python interpreter. It must import and re-execute your script from the beginning to learn about your functions and variables.

##### What Happens Without the Guard
Without the guard clause, the spawning process triggers a disastrous chain reaction:

   1. Main Process Starts: Python runs your script from top to bottom.
   2. Creation: It hits the line `p = Process(target=my_func)` and `p.start()`.
   3. Spawn Child 1: A new Python process launches and imports your script to load `my_func`.
   4. The Loop Begins: While importing, Child 1 executes the script from top to bottom. It hits the exact same `p.start()` line.
   5. Spawn Child 2: Child 1 launches Child 2.
   6. Crash: This repeats infinitely until your system runs out of memory or throws a `RuntimeError`. 

##### How the Guard Fixes It
The `__name__` variable tells Python the context of the current file execution:

* In the Main Process, `__name__` is automatically set to `"__main__"`.
* In the Child Process, because the file is being imported, `__name__` is set to the filename (e.g., `"myscript"`). 

By wrapping your process-starting code in `if __name__ == '__main__':`, you ensure that only the original script can launch new processes. When child processes import the file, the condition evaluates to `False`, allowing them to safely load your functions without launching subprocesses of their own. 

##### Visualizing the Execution Flow

```
[Main Process] (__name__ == '__main__')
   │
   ├── Runs top-level code
   ├── Hits the "if __name__ == '__main__':" block (TRUE)
   │     └── Launches Child Process
   │
   V
[Child Process] (__name__ == 'script_name')
   │
   ├── Imports and runs top-level code (defines functions)
   └── Hits the "if __name__ == '__main__':" block (FALSE)
         └── Skips launching code -> Safely executes assigned task
```

#### Pool.apply()
In Python's multiprocessing module, `Pool.apply()` submits a single task to a worker process and blocks execution until that task is completely finished. 
Because it blocks the main program, it runs tasks sequentially (one after the other), meaning it does not provide any actual parallelism. 

##### Key Characteristics

* Blocking: The main process stops and waits for the worker process to finish the task.
* Single Argument: It accepts a function and its arguments, passing them to a single worker.
* No Parallelism: Calling `Pool.apply()` in a loop runs tasks one by one, mimicking normal synchronous execution. 

##### Code Example

```python
import multiprocessingimport time
def worker_task(x):
    print(f"Processing {x}")
    time.sleep(1)
    return x * 2
if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        # This will take 3 seconds total because apply() blocks
        res1 = pool.apply(worker_task, args=(1,))
        res2 = pool.apply(worker_task, args=(2,))
        res3 = pool.apply(worker_task, args=(3,))
        
        print(f"Results: {res1}, {res2}, {res3}")
```

##### When to Use It
You should rarely use `Pool.apply()`. It is only useful when you specifically need to offload a single, heavy CPU-bound task to a background process but cannot move forward with your main program until you get that specific result. 

##### Alternatives for True Parallelism
* `Pool.apply_async()`: Non-blocking version of apply(). It submits the task and immediately lets the main program continue, returning a result object you can check later. 
* `Pool.map()`: Parallel version of Python's built-in `map()`. It splits an iterable of inputs across all available worker processes to run them simultaneously. 



## Context Manager

A context manager in Python is a resource-management tool that ensures setup and cleanup operations are executed automatically around a block of code, most commonly utilized via the `with` statement. 
### Why Use Context Managers

* Prevent leaks: They guarantee resource release.
* Handle errors: They clean up even if code crashes.
* Improve readability: They eliminate messy `try...finally ` blocks. 

------------------------------
### Common Built-In Examples

* File handling: Automatically closes a file after reading or writing.
  
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")

* Thread locks: Automatically acquires and releases a lock to prevent race conditions.

import threadinglock = threading.Lock()
with lock:
    # Critical section of code
    pass

```

------------------------------
### How to Create Custom Context Managers
You can build your own context managers using two primary methods:
#### 1. The Class-Based Approach
A class becomes a context manager by implementing two magic methods: 

* `__enter__`: Sets up the resource and optionally returns an object.
* `__exit__`: Cleans up the resource. It accepts three arguments (`exc_type`, `exc_value`, `traceback`) to handle exceptions. 

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to swallow exceptions, False to propagate them
        return False 
with ManagedFile("test.txt") as f:
    f.write("Custom context manager execution.")
```

#### 2. The Generator-Based Approach (contextmanager decorator)

The `contextlib` module provides a simpler way using a generator function. 

* Code before the yield statement acts as the `__enter__` logic.
* The `yield` statement provides the object to the as variable.
* Code after the yield statement acts as the `__exit__` logic. 

```python
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    try:
        file = open(filename, 'w')
        yield file
    finally:
        file.close()
with open_managed_file("test.txt") as f:
    f.write("Generator context manager execution.")
```
------------------------------


## Python Error Handling