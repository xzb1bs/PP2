def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

s = input()
result = reverse_words(s)
print("Reversed words sentence:", result)
