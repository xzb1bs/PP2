def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example of using the function
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed words sentence:", result)
