import re

def test(string):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_case_string = pattern.sub('_', string).lower()
    return snake_case_string

camel_s = input()
snake_s = test(camel_s)

