# In Python, a threading.Semaphore is a synchronization primitive used to limit access to a shared resource by a specific number of concurrent threads. 
# It manages an internal counter that decreases when a thread acquires it and increases when a thread releases it.

from threading import Thread, BoundedSemaphore
import time


semaphore = BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number} is trying to access!")
    with semaphore:
        print(f"{thread_number} is granted access!")
        time.sleep(10)
        print(f"{thread_number} is now releasing!")


if __name__ == "__main__":

    num_of_threads = 10
    threads = []
    for i in range(num_of_threads):

        thread = Thread(target = access, args=(i, ))
        threads.append(thread)

    # start threads
    start = time.perf_counter()
    for thread in threads:
        thread.start()

    # join thread, wait for them to complete
    for thread in threads:
        thread.join()

    print("End main.")
