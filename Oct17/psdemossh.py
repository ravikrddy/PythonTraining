"""single threaded"""
import paramiko


class CustomSSHClient_key:  # SSH key
    def __init__(self, host, user, key):
        self.host = host
        self.user = user
        self.key = key
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, username=self.user, key_filename=self.key)

    def check_output(self, job):
        stdin, stdout, stderr = self.ssh.exec_command(job)
        output = stdout.read()
        payload = output if output else stderr.read()
        return payload.decode()  # bytes into str

    def __del__(self):
        self.ssh.close()


class CustomSSHClient:  # Password
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.pwd)

    def check_output(self, job):
        stdin, stdout, stderr = self.ssh.exec_command(job)
        output = stdout.read()
        payload = output if output else stderr.read()
        return payload.decode()  # bytes into str

    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    # ssh_key = CustomSSHClient_key('ec2-54-174-65-221.compute-1.amazonaws.com', 'ubuntu', 'awskey.pem')
    # op_key = ssh_key.check_output('uname -a')
    # print(op_key)

    ssh = CustomSSHClient('10.108.4.22', 22, 'root', 'Z5!p@^2n2cA3s%U1')
    op = ssh.check_output('uname -a')
    print(op)
