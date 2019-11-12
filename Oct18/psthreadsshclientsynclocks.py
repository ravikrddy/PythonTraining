"""thread sync using lock"""

import threading
import logging
from time import sleep
import pyexcel
from psdemossh import CustomSSHClient

logging.basicConfig(format='%(threadName)s : %(message)s')
target_file = 'sshresponse.log'


class ThreadSSHClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job, lock):
        super().__init__(host, port, user, pwd)  # invoke overridden constructor
        self.job = job
        self.lock = lock
        self.t_name = threading.current_thread().name
        self.task_runner()

    def task_runner(self):
        payload = self.check_output(self.job)
        caption = f'{self.t_name} ran {self.job} @ {self.host}'

        logging.warning('check for the lock')

        with self.lock:
            logging.warning('acquired the lock')
            with open(target_file, 'a') as fw:
                # critical section
                sleep(1)
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload + '\n')
            logging.warning('releases the lock')


def main():
    sheet = pyexcel.get_sheet(file_name='hosts.xlsx')
    lock_object = threading.Lock()  # sync using lock
    for ssh_host_info in sheet:
        ssh_host_info.append(lock_object)
        threading.Thread(target=ThreadSSHClient, args=ssh_host_info).start()


if __name__ == '__main__':
    main()
