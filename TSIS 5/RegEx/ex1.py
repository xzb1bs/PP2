import re

def test(string):
    pattern = 'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

s = input()
string = test(s)
print(string)
