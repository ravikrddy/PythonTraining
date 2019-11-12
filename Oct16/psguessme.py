import random
i=0
while i<3:
    i = i+1
    n = int(input('enter the number between 1 to 3:'))
    print(n)
    print('random number:',random.randint(1,3))
    if n==random.randint(1,3):
        print('Won')
        break
    else:
        continue