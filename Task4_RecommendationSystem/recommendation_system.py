import pandas as pd
import random

# Load dataset
movies = pd.read_csv("movies.csv")

print("====================================")
print("    MOVIE RECOMMENDATION SYSTEM")
print("====================================\n")

# Show available movies
print("Available Movies:\n")

for movie in movies["Movie"]:
    print("-", movie)

print()

# User input
favorite_movie = input("Enter your favorite movie: ")

# Find movie genre
movie_data = movies[movies["Movie"].str.lower() == favorite_movie.lower()]

if not movie_data.empty:

    genre = movie_data.iloc[0]["Genre"]

    print(f"\n🎬 Recommended {genre} Movies For You:\n")

    recommendations = movies[
        (movies["Genre"] == genre) &
        (movies["Movie"].str.lower() != favorite_movie.lower())
    ]

    recommendation_list = recommendations["Movie"].tolist()

random.shuffle(recommendation_list)

for movie in recommendation_list[:3]:
    print(">", movie)

else:
    print("* Movie not found. Please try another movie.")
