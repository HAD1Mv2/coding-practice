from threading import Thread
import time

path = "data/text.txt"
text = ""

def read_file():

    global path, text
    while True:
        with open(path, 'r') as f:
            text = f.read()

        time.sleep(3)

def printloop():
    for x in range(30):
        print(text, " ", x)
        time.sleep(1)

if __name__ == "__main__":

    t1 = Thread(target=read_file, daemon=True) # a daemon thread will die after the main thread die
    t2 = Thread(target=printloop)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End main")

    
