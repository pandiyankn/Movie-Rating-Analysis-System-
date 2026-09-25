import pandas as pd
import numpy as np


class MovieAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    # =========================================
    # Basic Information
    # =========================================

    def basic_information(self):

        return {
            "total_movies": len(self.df),
            "total_genres": self.df["Genre"].nunique(),
            "average_rating": self.df["Rating"].mean()
        }

    # =========================================
    # Average Rating - NumPy
    # =========================================

    def average_rating(self):

        ratings = self.df["Rating"].to_numpy()

        return np.mean(ratings)

    # =========================================
    # Median Rating - NumPy
    # =========================================

    def median_rating(self):

        ratings = self.df["Rating"].to_numpy()

        return np.median(ratings)

    # =========================================
    # Highest Rating
    # =========================================

    def highest_rating(self):

        return self.df["Rating"].max()

    # =========================================
    # Lowest Rating
    # =========================================

    def lowest_rating(self):

        return self.df["Rating"].min()

    # =========================================
    # Rating Statistics
    # =========================================

    def rating_statistics(self):

        ratings = self.df["Rating"].to_numpy()

        return {
            "average": np.mean(ratings),
            "median": np.median(ratings),
            "maximum": np.max(ratings),
            "minimum": np.min(ratings),
            "standard_deviation": np.std(ratings)
        }

    # =========================================
    # Highest Rated Movies
    # =========================================

    def highest_rated_movies(self, limit=5):

        return (
            self.df
            .sort_values(
                by="Rating",
                ascending=False
            )
            .head(limit)
        )

    # =========================================
    # Lowest Rated Movies
    # =========================================

    def lowest_rated_movies(self, limit=5):

        return (
            self.df
            .sort_values(
                by="Rating",
                ascending=True
            )
            .head(limit)
        )

    # =========================================
    # Genre-wise Average Rating
    # =========================================

    def genre_wise_rating(self):

        return (
            self.df
            .groupby("Genre")["Rating"]
            .mean()
            .sort_values(
                ascending=False
            )
        )

    # =========================================
    # Number of Movies by Genre
    # =========================================

    def movies_by_genre(self):

        return (
            self.df
            .groupby("Genre")
            .size()
            .sort_values(
                ascending=False
            )
        )

    # =========================================
    # Movies Released Per Year
    # =========================================

    def movies_by_year(self):

        return (
            self.df
            .groupby("Release_Year")
            .size()
            .sort_index()
        )

    # =========================================
    # Search Movie
    # =========================================

    def search_movie(self, movie_name):

        movie_name = movie_name.lower()

        return self.df[
            self.df["Movie"]
            .str.lower()
            .str.contains(movie_name)
        ]

    # =========================================
    # Filter by Genre
    # =========================================

    def filter_by_genre(self, genre):

        genre = genre.lower()

        return self.df[
            self.df["Genre"]
            .str.lower()
            == genre
        ]

    # =========================================
    # Filter by Rating
    # =========================================

    def filter_by_rating(self, minimum_rating):

        return self.df[
            self.df["Rating"]
            >= minimum_rating
        ]