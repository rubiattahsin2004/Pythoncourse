starts_with = lambda text, sub: text.startswith(sub)

text = input("Enter a string: ")
sub = input("Enter the substring: ")

if starts_with(text, sub):
    print("The string starts with the given substring.")
else:
    print("The string does not start with the given substring.")
