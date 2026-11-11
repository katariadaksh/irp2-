def reverse_words(text):
    words = text.split()
    return " ".join(words[::-1])

text = input("Enter a sentence: ")
print(reverse_words(text))