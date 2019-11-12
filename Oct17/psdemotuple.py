"""
tuple aka readonly list
immutable object
"""
items = (2.2, 1.2, .98, 3, 2, 4, 5, 'alpha', 'beta', 'charlie')

#items[3]=333

print(items)

print(items[-4])  # indexing

for item in items[-4:]:  # slicing, iterate
    print(item)

n=(1000)
print(n)

m=(1000,)
print(m)
