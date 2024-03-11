def write_f(f_name, my_list):
    f = open(f_name, 'w')
    for i in my_list:
        f.write(i) 



f_name = "ex5_text.txt"
my_list = []
str = input()
my_list.append(str)
write_f(f_name, my_list)
