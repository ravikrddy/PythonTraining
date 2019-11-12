def copy(src, dest):
    try:
        fp = open(src)
        fw = open(dest, 'w')
        fw.write(fp.read())
        fp.close()
        fw.close()
        print('copied')
    except(FileNotFoundError, IOError) as err:
        print('Error')


"""demo for the context manager"""


def copy_python_way(src, dest):
    try:
        with open(src) as fp, open(dest, 'w') as fw:  # context manager
            fw.write(fp.read())
            print('copied')
    except(FileNotFoundError, IOError) as err:
        print('Error')


copy_python_way('listing.dat', 'content.txt')
