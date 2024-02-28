import re

def match(input_str):
    pattern = re.compile(r'a+b*')

    if pattern.fullmatch(input_str):
        print("Yes")
    else:
        print("No")

str = input()
match(str)
