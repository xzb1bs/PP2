import os

def check_path(path):
    if os.path.exists(path):
        print(f"Путь '{path}' существует.")
        if os.path.isfile(path):
            print(f"Это файл. Имя файла: {os.path.basename(path)}")
            print(f"Директория файла: {os.path.dirname(path)}")
        elif os.path.isdir(path):
            print("Это директория.")
    else:
        print(f"Путь '{path}' не существует.")

if __name__ == "__main__":
    path = input()
    check_path(path)
