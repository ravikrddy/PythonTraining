"""function variable length argument"""
import zipfile
import tarfile
import glob  # wild card selection


def make_zip(archive_name, *args):
    with zipfile.ZipFile(archive_name, mode='w') as zf:
        for file_name in args:
            zf.write(file_name)
            print(f'{file_name}: added to zip')


def make_tar(archive_name, *args):
    with tarfile.open(archive_name, mode='w') as tf:
        for file_name in args:
            tf.add(file_name)
            print(f'{file_name}: added to tar')


make_zip('src.zip', *glob.glob(' *.py'))
make_tar('src.tar', *glob.glob('*.py'))
