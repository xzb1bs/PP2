import re

def test(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

s = input()
string = test(s)
print(string)