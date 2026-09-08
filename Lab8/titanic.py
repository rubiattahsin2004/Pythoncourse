import pandas as pd
import numpy as np


file_path = r"D:\PYTHON\Python course aiub\LAB 8\Titanic-Dataset.csv"

df = pd.read_csv(file_path)



print("\nDataset Information:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())    
