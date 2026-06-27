from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):

    while True:
        # q.get will block the code when q still empty
        value = q.get()
        
        # processing

        # adding lock so the threads not try to print the lines at the same times 
        # (there is a pontential two threads print at the same time thus two print statement could appear in a single line (no newline)) 
        with lock:
            print(f"in {current_thread().name} got {value}")

        # In Python, q.task_done() is a method used by queue consumer threads (or coroutines) to signal that a previously retrieved task has been completely processed.
        # It works hand-in-hand with q.join() to let your main program know exactly when all work in a queue is finished.
        # If you forget to call task_done(), the counter will never hit zero, and q.join() will hang forever. If you call it too many times, Python will throw a ValueError.
        q.task_done()

if __name__ == "__main__":

    # Queue use to pass data in multithreads safely (avoid race condition)
    q: Queue = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))

        # daemon threads is background thread that will die when the main thread die, even if the sub threads is an infinite loop
        # if daemon == False, when the main thread dies, the sub-threads will still running (since we use infinite loop)
        # if we set daemon == False, we must set some stopping condition under the infinite loop so that it can stop
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    # Block the main thread so that the main program is not continue to the next line of code and wait for the sub threads to finish first
    q.join()

    print("End main.")