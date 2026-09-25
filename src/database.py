import pandas as pd

from src.models import Movie, MovieDatabase


class MovieDataManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.database = MovieDatabase()

    def load_movies(self):
        df = pd.read_csv(self.file_path)

        for _, row in df.iterrows():

            movie = Movie(
                movie_id=row["Movie_ID"],
                movie=row["Movie"],
                genre=row["Genre"],
                rating=row["Rating"],
                release_year=row["Release_Year"],
                reviews=row["Reviews"]
            )

            self.database.add_movie(movie)

        return self.database

    def get_database(self):
        return self.database
    