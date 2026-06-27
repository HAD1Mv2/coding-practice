import os
import time
from multiprocessing import Process


def some_process(n: int):

    # some process taking 1 second
    time.sleep(1)

    print(f"Process {n} done")


if __name__ == '__main__':

    num_of_processes = os.cpu_count()
    assert isinstance(num_of_processes, int)

    # Sequential
    start = time.perf_counter()
    for i in range(num_of_processes):
        some_process(i)
    end = time.perf_counter()
    print(f"sequential process end in {end-start} seconds.")


    # Multiprocess 
    # Instantiate the process
    start = time.perf_counter()

    processes: list = []

    for i in range(num_of_processes):
        p = Process(target=some_process, args=(i,))
        processes.append(p)

    # Start processes
    for p in processes:
        p.start()

    # Process.join() is a blocking method to ensure all processes finish first before continue to run next code line
    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f"multiprocess end in {end-start} seconds.")




