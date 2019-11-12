import multiprocessing
from random import randint

def task_set(value):  # child process function
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().pid
    print(p_name, ':', p_id, 'received: ', value)


def main():  # parent process
    parent = multiprocessing.current_process()
    print(parent.name, ':', parent.pid)
    for item in range(1, 6):
        multiprocessing.Process(target=task_set, name='p' + str(item), args=(randint(1, 100),)).start()
    for child in multiprocessing.active_children():  # to wait for the child to complete
        child.join()


if __name__ == '__main__':
    main()
