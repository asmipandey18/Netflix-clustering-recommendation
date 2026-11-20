## load and clean
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print("Original dataset shape:", df.shape)

print("\nMissing values before cleaning:")
print(df.isnull().sum())

text_columns = ["director", "cast", "country", "date_added", "rating", "duration"]
for column in text_columns:
    df[column] = df[column].fillna("Unknown")

print("\nMissing values after cleaning:")
print(df.isnull().sum())
print("Duplicates:", df["show_id"].duplicated().sum())
print("\nContent type counts:")
print(df["type"].value_counts())
df.head()

## duration and rating features
# "Unknown" back to missing, then pull the number out of "90 min" / "2 Seasons"
df["duration"] = df["duration"].replace("Unknown", pd.NA)
df["duration_num"] = df["duration"].str.extract(r"(\d+)", expand=False).astype(float)

# Fill missing durations with the median of the same type (Movie or TV Show)
df["duration_num"] = df.groupby("type")["duration_num"].transform(lambda s: s.fillna(s.median()))

# Group the many rating labels into audience groups
rating_map = {
    "G": "Kids", "TV-Y": "Kids", "TV-G": "Kids", "TV-Y7": "Kids", "TV-Y7-FV": "Kids",
    "PG": "Teens", "TV-PG": "Teens", "PG-13": "Teens", "TV-14": "Teens",
    "R": "Adults", "TV-MA": "Adults", "NC-17": "Adults",
}
df["rating_group"] = df["rating"].map(rating_map).fillna("Other")

print(df["rating_group"].value_counts())
print(df.groupby("type")["duration_num"].describe().round(1)) 