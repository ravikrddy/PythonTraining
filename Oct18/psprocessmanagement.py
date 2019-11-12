"""demo pipes"""
import subprocess

# op = subprocess.check_output(['python', 'psdemohttp.py'])
# print(op)
cat = subprocess.Popen(['cat', '/etc/passwd'], stdout=subprocess.PIPE)
tr = subprocess.Popen(['tr', 'a-z', 'A-Z'], stdin=cat.stdout, stdout=subprocess.PIPE)
nl = subprocess.Popen(['nl'], stdin=tr.stdout, stdout=subprocess.PIPE)

for item in nl.communicate():
    if item:
        print(item.decode())
