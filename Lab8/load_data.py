import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myseries = pd.Series(calories)

print(myseries)

total_calories = myseries.sum()

print("Total calories:", total_calories)
