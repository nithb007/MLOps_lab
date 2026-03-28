import pandas as pd
import pickle
import os

from sklearn.metrics.pairwise import cosine_similarity

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/processed/ratings_clean.csv")

user_item = df.pivot_table(index="user_id", columns="movie_id", values="rating").fillna(0)

similarity = cosine_similarity(user_item)

with open("models/user_similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

print("user_similarity.pkl created!")