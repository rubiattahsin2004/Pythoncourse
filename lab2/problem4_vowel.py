ch = input("Enter a character: ").lower()

if len(ch) != 1:
    print("Please enter only one character.")
elif ch in ['a', 'e', 'i', 'o', 'u']:
    print(ch, "is a Vowel.")
else:
    print(ch, "is Not a Vowel.")
