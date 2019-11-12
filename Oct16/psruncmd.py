"""demo for the bytes"""

import sys
import subprocess  # process management

if sys.platform in ['linux', 'darwin']:
    # cmd = ['ifconfig']
    cmd = ['ls', '-l', '/etc/passwd']
elif sys.platform == 'win32':
    cmd = ['ipconfig']
else:
    raise OSError('Unsupported OS')

op = subprocess.check_output(cmd)
# print(op)
print(op.decode())  # bytes into unicode
