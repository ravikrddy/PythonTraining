import math
import sys
import pprint


class SystemInformation:
    def __init__(self):
        print(self, 'I am in constructor')

    def demo(self):
        print(self,'><')

    def __del__(self):
        print(self, 'I am destructor')


si = SystemInformation()
print(si)
si.demo()
# print(SystemInformation)
# print(__name__)  # __main__ is the default python namespace (logical container)
# print(math.__name__)
# print(sys.__name__)
# print(pprint.PrettyPrinter)
