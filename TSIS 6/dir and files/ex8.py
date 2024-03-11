import os

def check_path(path):
    path_clone = path
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"path '{path}' exists.")
            print(f"name of this file: {os.path.basename(path)}")
        os.remove(path_clone)
    else:
        print(f"Путь '{path}' не существует.")


path = input()
check_path(path)
