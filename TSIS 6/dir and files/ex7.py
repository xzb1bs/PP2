def copy_file(first_file, second_file):
    f = open(first_file, 'r') 
    o = open(second_file, 'w') 
    str = f.read()
    o.write(str)
       

first_file = "ex7(1)_text.txt"
second_file = "ex7(2)_text.txt"
copy_file(first_file, second_file)
