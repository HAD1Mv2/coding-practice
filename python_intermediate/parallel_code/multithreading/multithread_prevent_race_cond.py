from threading import Thread, Lock
import time

database_value = 0

def add_database_value(lock):

    global database_value

    # add lock to prevent other thread to access database_value simultaneously
    # lock.acquire()

    # using lock as a context manager
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        # update database value
        database_value = local_copy

    # release lock
    # lock.release()

if __name__ == '__main__':

    lock = Lock()
    print(f"start database_value {database_value}")

    thread1 = Thread(target=add_database_value, args=(lock,))
    thread2 = Thread(target=add_database_value, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"current database_value {database_value}")