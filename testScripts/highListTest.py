import numpy as np
from multiprocessing import Process, Condition, Event
from time import sleep
import psutil


def read_arr(arr, done, stop):
    with done:
        S = np.sum(arr)
        print(S)
        done.notify()
    while not stop.is_set(): 
        sleep(1)


def main():
    # Create a large array
    print('Available before xlList (MiB):', psutil.virtual_memory().available / 1024 ** 2)
    input("Press Enter...")
    xlList = np.random.random(2**28)
    print(len(xlList))
    print(xlList[0], xlList[1])
    print('Available before Process (MiB):', psutil.virtual_memory().available / 1024 ** 2)
    input("Press Enter...")
    done = Condition()
    stop = Event()
    p = Process(target=read_arr, args=(xlList, done, stop))
    with done:
        p.start()
        done.wait()
    print('Available with Process (MiB):', psutil.virtual_memory().available / 1024 ** 2)
    input("Press Enter...")
    stop.set()
    p.join()

if __name__ == '__main__':
    main()