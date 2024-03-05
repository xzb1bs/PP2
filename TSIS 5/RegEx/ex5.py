import re

def test(s):
    pattern = r'a.*b$'
    if re.match(pattern, s):
        return True
    else:
        return False

s = input()
string = test(s)
print(string)