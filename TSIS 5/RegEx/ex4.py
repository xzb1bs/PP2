import re

def test(s):
    pattern = re.compile(r'[A-Z][a-z]+')
    sequences = pattern.findall(s)
    return sequences


s = input()
string = test(s)
print(string)