import re

s = 'the python and the perl scripting'
pattern1 = 'P.+N'  # greedy match -> 'python and the perl scriptin'
pattern = 'P.+?N'  # non-greedy match -> 'python'

m = re.search(pattern, s, re.I)
if m:
    print(m)
    print('match string: ', m.group())
    print(m.start())
    print(m.end())
    print()
else:
    print('failed to match')

for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
    print()
