"""
Package manager

name
Version

__init__()
get_information()
"""


class PackageManager:
    def __init__(self, name, version):
        self.__name = name #private attribute
        self.version = version

    def __get_information(self): #private method
        print('name: ', self.__name)
        print('version: ', self.version)

    def wrapper(self): #public method
        self.__get_information()


pm = PackageManager('pip', '2.2.18')
#pm.__get_information()
pm.wrapper()

#print(pm.__name)  # only public members cann't be accessible from outside of the class
