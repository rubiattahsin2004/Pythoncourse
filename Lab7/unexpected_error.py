try:
    # Create a file
    file = open("example.txt", "x")
    file.write("This is the first line.\n")
    file.close()

    # Write to the file
    file = open("example.txt", "w")
    file.write("This content is written using write mode.\n")
    file.close()

    # Append content to the file
    file = open("example.txt", "a")
    file.write("This is additional content using append mode.\n")
    file.close()

    # Read the file
    file = open("example.txt", "r")
    content = file.read()
    print("File Content:")
    print(content)
    file.close()

except FileExistsError:
    print("Error: The file already exists.")

except FileNotFoundError:
    print("Error: The file was not found.")

except Exception as e:
    print("An unexpected error occurred:", e)
