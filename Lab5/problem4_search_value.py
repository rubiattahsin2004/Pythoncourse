numbers = [10, 20, 30, 40, 50]
value = int(input("Enter value to search: "))

found = False

for number in numbers:
    if number == value:
        found = True
        break

if found:
    print("Value found")
else:
    print("Value not found")
