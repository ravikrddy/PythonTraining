for item in range(10):  # range
    print(item)

for item in range(1, 10):
    print(item)

for item in range(1, 10, -2):
    print(item)

items = [hex(item) for item in range(1, 11)]  # list comprehension
print(items)

temp = [i ** 2 for i in range(1, 11)]
print(temp)

temp = [i for i in range(1, 11) if i % 2]  # compound list comprehension
print(temp)

temp={hex(i) for i in range(1,11)} #set comprehension
print(temp)

temp={i:hex(i) for i in range(1,11)} #dict comprehension
print(temp)