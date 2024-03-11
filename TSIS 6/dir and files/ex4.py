def count(f_name):
    try:
        with open(f_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
        print(num_lines)
    except FileNotFoundError:
        print("file nit found")


file_name = "ex4_text.txt"
count(file_name)
