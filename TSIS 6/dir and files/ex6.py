import string

def create_files():
    alphabet = string.ascii_uppercase
    
    for letter in alphabet:
        file_name = f"{letter}.txt"
        f = open(file_name, 'w') 

if __name__ == "__main__":
    create_files()
