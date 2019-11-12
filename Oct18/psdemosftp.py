"""sftp client"""
from psdemossh import CustomSSHClient
from math import pi, sin


class SFTPClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd):
        super().__init__(host, port, user, pwd)  # invoke overridden constructor
        self.sftp = self.ssh.open_sftp()

    def upload(self, src, dest):
        self.sftp.put(src, dest)
        print(f'{src} uploaded as {dest}')

    def __del__(self):
        self.sftp.close()
        super().__del__()


if __name__ == '__main__':
    ftp = SFTPClient('10.108.4.22', 22, 'root', 'Z5!p@^2n2cA3s%U1')
    ftp.upload('psdemosftp.py', 'ftpcli.py')
    print(ftp.check_output('stat ftpcli.py'))
