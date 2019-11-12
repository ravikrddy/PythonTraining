s='root:x:0:0:root:/root:/bin/bash'
delimiter=':'

items=s.split(delimiter)
print(items)

print(s.split(':')[0]) #indexing
print(s.split(':')[1:]) #slicing

for item in items: #iterate
    print(item)
