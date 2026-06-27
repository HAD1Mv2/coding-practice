from multiprocessing import Process, Value, Array, Lock
import time


# Value and Array are objects used to access same data between Processes in runtime
# Value is used to pass single value, Array is used to pass an array

def add_100(number, lock):

    for i in range(100):
        time.sleep(0.01)

        # using lock as context manager
        with lock:
            number.value +=1

# add 100 for Array
def add_100_in_array(numbers, lock):

    for i in range(100):
        time.sleep(0.01)

        # iterate using index, don't access the value directly using variable 
        # since the variable will be treated as local variable hence it won't update the array
        for i in range(len(numbers)):
            with lock:
                numbers[i] +=1

if __name__ == "__main__":

    # Create lock to prevent race condition
    lock = Lock()

    # # Passing single value (Value) between processes
    # # Syntax -> Value(data type, value)
    # shared_value = Value('i', 0)  # 'i' as in int
    # print("Value at beginnning is ", shared_value.value)

    # p1 = Process(target=add_100, args=(shared_value, lock))
    # p2 = Process(target=add_100, args=(shared_value, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print("Value at the end is ", shared_value.value)
    

    # ==================================================================#


    # Passing Array between processes
    # Syntax -> Array(data type, size_or_initializer)
    # If size_or_initializer is an integer, then it determines the length of the array, and the array will be initially zeroed. 
    # Otherwise, size_or_initializer is a sequence which is used to initialize the array and whose length determines the length of the array.

    shared_array = Array('d', [0.0, 100.0, 200.0])  # 'i' as in int
    print("Value at beginnning is ", shared_array[:]) # ucan use index (shared_array[2]) or index slice to get the array

    p1 = Process(target=add_100_in_array, args=(shared_array, lock))
    p2 = Process(target=add_100_in_array, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Value at the end is ", shared_array[:])
