import re

pattern = ' +'

for line in open('listing.dat'):
    print(re.split(pattern, line))

sizes = [int(re.split(pattern, line)[4]) for line in open('listing.dat')]  # list comprehension
print(sizes)
print(max(sizes))
print(min(sizes))
print(sum(sizes))
print(sum(sizes) / len(sizes))
