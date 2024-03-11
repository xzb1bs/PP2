def write_f(f_name, my_list):
    with open(f_name, 'w') as file:
        for item in my_list:
            file.write(item) 


if __name__ == "__main__":
    f_name = "ex5_text.txt"
    my_list = []
    item = input()
    my_list.append(item)
    write_f(f_name, my_list)
