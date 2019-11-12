import re

s = '_mbsetupuser:*:248:248:Setup User:/var/setup:/bin/bash'
pattern = ':'
replacement = ','

s2 = re.sub(pattern, replacement, s)
s3 = re.sub('[AEIOU]', '*', s2, flags=re.I)
s4 = re.sub('[AEIOU]', '*', s2, flags=re.I, count=3)

print(s)
print(s2)
print(s3)
print(s4)
