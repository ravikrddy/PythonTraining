"""variable len args"""


def demo(*args):
    print(args)


demo()
demo(123)
demo(1, 2, 'iii', 4, 5)

items = [11, 22, 33]
demo(items)
demo(*items)  # content of the objects as argument

items = (11, 22, 33)
demo(items)
demo(*items)


def compute(a, b, c):
    print(a + b + c)


items = [11, 22, 33]
compute(items[0], items[1], items[2])
compute(*items)

def compute_args(*args):
    temp=0
    for item in args:
        temp=temp+item
    print(temp)

items = [11, 22, 33, -66]
compute_args(*items)
