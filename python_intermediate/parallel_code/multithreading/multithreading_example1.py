from threading import Thread
import time

def some_process(n: int):

    start = time.perf_counter()
    # some process taking n second
    time.sleep(n)
    end = time.perf_counter()

    print(f"Process {n} done in {end-start} seconds")

if __name__ == '__main__':

    threads = []
    num_of_threads = 5

    # create threads
    for i in range(num_of_threads):

        thread = Thread(target = some_process, args=(i, ))
        threads.append(thread)

    # start threads
    start = time.perf_counter()
    for thread in threads:
        thread.start()

    # join thread, wait for them to complete
    for thread in threads:
        thread.join()

    end = time.perf_counter()
    print(f"All threads end in {end-start} seconds.")
    print("End main.")