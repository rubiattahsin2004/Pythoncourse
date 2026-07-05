items = ['aca', 'xyz', 'aba', '1221']
count = 0

for item in items:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1

print(count)
