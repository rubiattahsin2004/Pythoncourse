def palindrome(text):
    if text == text[::-1]:
        return True
    return False

word = input("Enter a string: ")

if palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")
