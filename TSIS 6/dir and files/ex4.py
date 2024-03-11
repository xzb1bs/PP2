def count(f_name):
    f = open(f_name, 'r') 
    lines = f.readlines()
    num_lines = len(lines)
    print(num_lines)
    

f_name = "ex4_text.txt"
count(f_name)
