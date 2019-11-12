class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def get_info(self):
        print('first name: ', self.fn)
        print('last name: ', self.ln)


if __name__ == '__main__':
    p = Person('ravi', 'kumar')
    p.get_info()
