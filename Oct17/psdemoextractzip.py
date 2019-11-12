import zipfile
import tarfile
import os


def extract_zip(archive_name, target_path):
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    with zipfile.ZipFile(archive_name) as zf:
        zf.extractall(target_path)
    print('zip extracted')


def extract_tar(archive_name, target_path):
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    with tarfile.open(archive_name) as tf:
        tf.extractall(target_path)
    print('tar extracted')


extract_tar('src.tar', target_path='temp')
