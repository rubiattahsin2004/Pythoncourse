import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")
print("First 5 rows of the dataset:")
print(df.head())
# 1. LINE PLOT
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length")
plt.plot(df.index, df["petal_length"], label="Petal Length")
plt.title("Line Plot of Sepal Length and Petal Length")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.grid()
plt.show()
# 2. SCATTER PLOT
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="sepal_length",
    y="petal_length",
    hue="species"
)

plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.show()
#bar plot
species_count = df["species"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(species_count.index, species_count.values)

plt.title("Number of Flowers in Each Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
# 4. HISTOGRAM

plt.figure(figsize=(8, 5))
plt.hist(df["sepal_length"], bins=10, edgecolor="black")

plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()
# 5. PIE CHART

plt.figure(figsize=(7, 7))
plt.pie(
    species_count.values,
    labels=species_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Percentage of Each Iris Species")
plt.show()

# 6. SUBPLOTS

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Subplot 1: Line Plot
axes[0, 0].plot(df.index, df["sepal_length"])
axes[0, 0].set_title("Sepal Length Line Plot")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Sepal Length")

# Subplot 2: Scatter Plot
axes[0, 1].scatter(df["sepal_length"], df["petal_length"])
axes[0, 1].set_title("Sepal vs Petal Length")
axes[0, 1].set_xlabel("Sepal Length")
axes[0, 1].set_ylabel("Petal Length")

# Subplot 3: Histogram
axes[1, 0].hist(df["petal_width"], bins=10, edgecolor="black")
axes[1, 0].set_title("Petal Width Histogram")
axes[1, 0].set_xlabel("Petal Width")
axes[1, 0].set_ylabel("Frequency")

# Subplot 4: Bar Chart
axes[1, 1].bar(species_count.index, species_count.values)
axes[1, 1].set_title("Species Count")
axes[1, 1].set_xlabel("Species")
axes[1, 1].set_ylabel("Count")

plt.tight_layout()
plt.show()
