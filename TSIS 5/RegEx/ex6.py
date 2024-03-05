import re

def test(s):
    pattern = r'[ ,.]'
    modified_string = re.sub(pattern, ':', s)
    return modified_string

s = input()
string = test(s)
print(string)