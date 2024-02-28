import re

def match_string(input_str):
    pattern = re.compile(r'a{1}b{2,3}')

    if pattern.fullmatch(input_str):
        print(f'Строка "{input_str}" соответствует шаблону.')
    else:
        print(f'Строка "{input_str}" не соответствует шаблону.')


s = input()
match_string(s)
