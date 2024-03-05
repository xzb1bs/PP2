import re

def test(s):
    pattern = re.compile(r'_(.)')
    camel_case_string = pattern.sub(lambda x: x.group(1).upper(), s)
    return camel_case_string

snake_s = input()
camel_s = test(snake_s)
print(camel_s)