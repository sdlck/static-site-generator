import os
import shutil

def copy_dir(src: str, dest: str) -> None:
    if not os.path.exists(src):
        raise Exception(f"source directory {src} not found")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    print(f"copying '{src}' to '{dest}'")
    for object in os.listdir(src):
        path = os.path.join(src, object)
        if os.path.isfile(path):
            print(f"file: '{object}'")
            shutil.copy(path, dest)
        if os.path.isdir(path):
            print(f"dir: '{object}'")
            new_dest = os.path.join(dest, object)
            copy_dir(path, new_dest)