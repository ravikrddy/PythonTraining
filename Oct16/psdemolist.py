import math
import decimal as d

# items=[]
items = [2.2, 'pam', 3.2, 'kimberly', 'pat', 'nick', .98, 1., 2, 3]

items[-2] = 'ii'  # update
items[3] = 'kim'

print(items)
# print(type(items))
# print(len(items))

items.append('citrix')
items.insert(4, 'bangalore')
print(items)

value = items.pop(-4)
print(value)

item = 'pat'
items.remove(item)  # first occurrence
print(items)

temp=[] #removing the items with 0.2 in decimal
for item in items:
    if type(item) is float:
        if d.Decimal(str(item))-d.Decimal(str(math.floor(item)))==d.Decimal('.2'):
            continue
    temp.append(item)
print(temp)
















