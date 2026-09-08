my_list = [10, 20, 30, 40, 50]

try:
    index = input("Enter the index: ")
    print("Element:", my_list[index])

except IndexError:
    print("Error: Index is out of range.")

except TypeError:
    print("Error: Index must be an integer.")
