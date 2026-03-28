import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/ratings.csv")

df = df.drop_duplicates()
df = df[df["rating"] >= 0]

df.to_csv("data/processed/ratings_clean.csv", index=False)

print("ratings_clean.csv created!")