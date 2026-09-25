import os

import pandas as pd
import matplotlib.pyplot as plt


class MovieVisualizer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

        self.output_folder = "output/charts"

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    # =========================================
    # Rating Distribution
    # =========================================

    def rating_distribution(self):

        plt.figure(figsize=(9, 5))

        plt.hist(
            self.df["Rating"],
            bins=8,
            edgecolor="black"
        )

        plt.title("Tamil Movie Rating Distribution")
        plt.xlabel("Rating")
        plt.ylabel("Number of Movies")

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "rating_distribution.png"
        )

        plt.savefig(path)
        plt.close()

        return path

    # =========================================
    # Genre-wise Average Rating
    # =========================================

    def genre_comparison(self):

        genre_ratings = (
            self.df
            .groupby("Genre")["Rating"]
            .mean()
            .sort_values(
                ascending=False
            )
        )

        plt.figure(figsize=(9, 5))

        genre_ratings.plot(
            kind="bar",
            edgecolor="black"
        )

        plt.title("Average Rating by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Average Rating")

        plt.xticks(rotation=45)

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "genre_comparison.png"
        )

        plt.savefig(path)
        plt.close()

        return path

    # =========================================
    # Movies Released Per Year
    # =========================================

    def movies_released_per_year(self):

        yearly_movies = (
            self.df
            .groupby("Release_Year")
            .size()
            .sort_index()
        )

        plt.figure(figsize=(10, 5))

        yearly_movies.plot(
            kind="bar",
            edgecolor="black"
        )

        plt.title("Tamil Movies Released Per Year")
        plt.xlabel("Release Year")
        plt.ylabel("Number of Movies")

        plt.xticks(rotation=45)

        plt.tight_layout()

        path = os.path.join(
            self.output_folder,
            "movies_released_per_year.png"
        )

        plt.savefig(path)
        plt.close()

        return path