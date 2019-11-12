items = {2.2, 1, 'kim', 2, 3, 4, 5, 'pat'} #set

items.add('citrix') #add
items.add('thinkpad')
items.add(3.1242)

items.remove('kim') #remove

items.update(0)

print(items)

for item in items:
    print(item)