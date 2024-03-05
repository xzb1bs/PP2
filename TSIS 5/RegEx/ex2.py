import re

def test(string):
    pattern = 'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

s = input()
string = test(s)
print(string)