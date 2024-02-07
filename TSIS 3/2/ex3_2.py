def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    reversed_word = cleaned_word[::-1]
    return cleaned_word == reversed_word

input_word = input()
result = is_palindrome(input_word)
print(f'Фраза "{input_word}" - {"палиндром" if result else "не палиндром"}')
