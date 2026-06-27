from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    # close(): Prevents any more tasks from being submitted to the pool. Once all the tasks have been completed the worker processes will exit.
    # join() : Wait for the worker processes to exit. One must call close() or terminate() before using join().

    # Pool will allocate a number of processes, split the input into several chunk and distribute it to the processes, no hassle. 
    result = pool.map(cube, numbers)

    # # to process single task to a worker process
    # result = pool.apply(cube, [numbers[0]])

    pool.close()
    pool.join()

    print(result)

