numbers = [10, 20, 30, 20, 50]
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print(result)
