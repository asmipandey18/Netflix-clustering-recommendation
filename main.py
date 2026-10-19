
import pandas as pd

# Load the Netflix dataset
df = pd.read_csv("netflix_titles.csv")

print("Original dataset shape:", df.shape)

# Check missing values before cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing text values
text_columns = [
    "director",
    "cast",
    "country",
    "date_added",
    "rating",
    "duration"
]

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Display dataset information
print("\nCleaned dataset shape:", df.shape)

# Display content type counts
print("\nContent type counts:")
print(df["type"].value_counts())

# Display the first five rows
print("\nFirst five rows:")
print(df.head())
