text = input("Enter a string: ")

words = text.split()
reversed_words = words[::-1]

print(" ".join(reversed_words))
