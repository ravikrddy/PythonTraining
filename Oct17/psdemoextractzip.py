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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tf, target_path)
    print('tar extracted')


extract_tar('src.tar', target_path='temp')
