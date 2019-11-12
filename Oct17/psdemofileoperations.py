fp = open('passwd.txt')
for temp in fp:
    print(temp, end='')
fp.close()
