def count_items(items):
    for item in sorted(set(items)):
        print(f"{item} => {items.count(item)}")

numbers = [10, 20, 30, 30, 30, 30, 20, 40]

count_items(numbers)
