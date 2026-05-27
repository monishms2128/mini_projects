import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# Load dataset
movies = pd.read_csv("movies.csv")

# Main Window
window = tk.Tk()
window.title("Movie Recommendation System")
window.geometry("700x600")
window.configure(bg="#1e1e1e")

# Title
title = tk.Label(
    window,
    text="🎬 Movie Recommendation System",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=20)

# Input Label
label = tk.Label(
    window,
    text="Enter Your Favorite Movie:",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

label.pack()

# Input Box
movie_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=30,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

movie_entry.pack(pady=10)

# Recommendation Area
result_area = tk.Text(
    window,
    height=15,
    width=60,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white"
)

result_area.pack(pady=20)

# Recommendation Function
def recommend_movies():

    favorite_movie = movie_entry.get()

    result_area.delete("1.0", tk.END)

    movie_data = movies[
        movies["Movie"].str.lower() == favorite_movie.lower()
    ]

    if not movie_data.empty:

        genre = movie_data.iloc[0]["Genre"]

        recommendations = movies[
            (movies["Genre"] == genre) &
            (movies["Movie"].str.lower() != favorite_movie.lower())
        ]

        recommendation_list = recommendations["Movie"].tolist()

        random.shuffle(recommendation_list)

        result_area.insert(
            tk.END,
            f"🎬 Recommended {genre} Movies:\n\n"
        )

        for movie in recommendation_list[:3]:

            result_area.insert(
                tk.END,
                f"👉 {movie}\n"
            )

    else:

        messagebox.showerror(
            "Error",
            "Movie not found in database."
        )

# Recommend Button
recommend_button = tk.Button(
    window,
    text="Recommend",
    font=("Arial", 14, "bold"),
    bg="#007acc",
    fg="white",
    activebackground="#005f99",
    activeforeground="white",
    command=recommend_movies
)

recommend_button.pack(pady=10)
footer = tk.Label(
    window,
    text="Developed by Monish | CODSOFT AI Internship",
    font=("Arial", 10),
    bg="#1e1e1e",
    fg="gray"
)

footer.pack(side="bottom", pady=10)
window.bind('<Return>', lambda event: recommend_movies())
# Run Window
window.mainloop()