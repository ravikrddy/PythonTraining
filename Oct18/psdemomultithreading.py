import threading
from time import sleep
from random import random


def worker(delay):  # thread function
    t_name = threading.current_thread().name
    # t_id = threading.current_thread().ident
    sleep(delay)
    print(t_name, 'waited for the: ', delay)


def main():  # main thread
    for item in range(1, 6):
        rand_value = random()
        t = threading.Thread(target=worker, args=(rand_value,), name='t' + str(item))
        t.start()
    print(threading.current_thread().name, 'prepares to terminate...')


if __name__ == '__main__':
    main();
