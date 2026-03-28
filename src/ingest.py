import pandas as pd
import numpy as np
import os
print("INGEST RUNNING")
os.makedirs("data/raw", exist_ok=True)

n_users = 50
n_movies = 100
n_ratings = 2000

data = {
    "user_id": np.random.randint(1, n_users, n_ratings),
    "movie_id": np.random.randint(1, n_movies, n_ratings),
    "rating": np.random.uniform(0, 5, n_ratings)
}

df = pd.DataFrame(data)
df.to_csv("data/raw/ratings.csv", index=False)

print("ratings.csv created!")