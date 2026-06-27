from threading import Thread
import time

database_value = 0

def add_database_value():

    global database_value

    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    # update database value
    database_value = local_copy

if __name__ == '__main__':

    print(f"start database_value {database_value}")

    thread1 = Thread(target=add_database_value)
    thread2 = Thread(target=add_database_value)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"current database_value {database_value}")
