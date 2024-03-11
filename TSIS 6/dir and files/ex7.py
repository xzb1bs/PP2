def copy_file(first_file, second_file):
    with open(first_file, 'r') as first:
        with open(second_file, 'w') as second:
            str = first.read()
            second.write(str)
       

first_file = "ex7(1)_text.txt"
second_file = "ex7(2)_text.txt"
copy_file(first_file, second_file)
