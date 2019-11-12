import re

pattern = 'bash$'

for line in open('passwd.txt'):
    if re.search(pattern, line, re.I):
        print(line, end='')
