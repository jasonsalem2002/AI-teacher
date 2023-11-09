# utils.py
import os

def setup_directories(base_dir, subdirs=["Texts", "Images"]):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    directories = {}
    for subdir in subdirs:
        dir_path = os.path.join(base_dir, subdir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        directories[subdir] = dir_path

    return directories
