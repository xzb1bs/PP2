import string

def create_files():
    alphabet = string.ascii_uppercase
    
    for letter in alphabet:
        file_name = f"{letter}.txt"
        f = open(file_name, 'w') 

create_files()
