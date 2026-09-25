class Movie:
    def __init__(
        self,
        movie_id,
        movie,
        genre,
        rating,
        release_year,
        reviews
    ):
        self.movie_id = movie_id
        self.movie = movie
        self.genre = genre
        self.rating = float(rating)
        self.release_year = int(release_year)
        self.reviews = int(reviews)

    def display(self):
        return (
            f"{self.movie} | "
            f"{self.genre} | "
            f"Rating: {self.rating} | "
            f"Year: {self.release_year}"
        )


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display(self):
        return f"{self.name} ({self.email})"


class Review:
    def __init__(
        self,
        review_id,
        user_id,
        movie_id,
        rating,
        comment=""
    ):
        self.review_id = review_id
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = float(rating)
        self.comment = comment

    def display(self):
        return (
            f"Review {self.review_id} | "
            f"Rating: {self.rating} | "
            f"{self.comment}"
        )


class MovieDatabase:
    def __init__(self):
        self.movies = []
        self.users = []
        self.reviews = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_user(self, user):
        self.users.append(user)

    def add_review(self, review):
        self.reviews.append(review)

    def get_movie_count(self):
        return len(self.movies)

    def get_user_count(self):
        return len(self.users)

    def get_review_count(self):
        return len(self.reviews)

    def search_movie(self, movie_name):
        movie_name = movie_name.lower()

        return [
            movie
            for movie in self.movies
            if movie_name in movie.movie.lower()
        ]

    def get_movies_by_genre(self, genre):
        genre = genre.lower()

        return [
            movie
            for movie in self.movies
            if movie.genre.lower() == genre
        ]

    def get_highest_rated_movie(self):
        if not self.movies:
            return None

        return max(
            self.movies,
            key=lambda movie: movie.rating
        )