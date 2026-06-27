from threading import Thread, Event

def my_func(event):
    print("Waiting for event to trigger ... \n")
    # trigger event
    event.wait()
    print("Performing action abc now ...")

if __name__ == "__main__":

    # instantiate event
    event = Event()

    t1 = Thread(target=my_func, args=(event, ))
    t1.start()

    input_ = input("Do you want to trigger the event ?(y/n) :")

    if input_ == "y":
        # start event
        event.set()

    # blocking main thread
    t1.join()
    print("End main thread")