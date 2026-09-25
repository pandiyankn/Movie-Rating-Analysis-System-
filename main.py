from src.database import MovieDataManager
from src.analysis import MovieAnalyzer
from src.visualization import MovieVisualizer


DATA_FILE = "data/movies.csv"


def print_line():
    print("-" * 70)


def display_movies(df):
    if df.empty:
        print("\nNo movies found.")
        return

    print()
    print(df.to_string(index=False))


def show_basic_information(analyzer):
    info = analyzer.basic_information()

    print("\n===== BASIC INFORMATION =====")
    print(f"Total Movies       : {info['total_movies']}")
    print(f"Total Genres       : {info['total_genres']}")
    print(f"Average Rating     : {info['average_rating']:.2f}")


def show_rating_statistics(analyzer):
    stats = analyzer.rating_statistics()

    print("\n===== RATING STATISTICS =====")
    print(f"Average Rating     : {stats['average']:.2f}")
    print(f"Median Rating      : {stats['median']:.2f}")
    print(f"Maximum Rating     : {stats['maximum']:.2f}")
    print(f"Minimum Rating     : {stats['minimum']:.2f}")
    print(f"Standard Deviation : {stats['standard_deviation']:.2f}")


def show_highest_rated(analyzer):
    print("\n===== TOP 5 HIGHEST-RATED MOVIES =====")

    movies = analyzer.highest_rated_movies(5)

    display_movies(movies)


def show_lowest_rated(analyzer):
    print("\n===== TOP 5 LOWEST-RATED MOVIES =====")

    movies = analyzer.lowest_rated_movies(5)

    display_movies(movies)


def show_genre_analysis(analyzer):
    print("\n===== GENRE-WISE AVERAGE RATING =====")

    result = analyzer.genre_wise_rating()

    print(result.to_string())


def show_movies_by_genre(analyzer):
    print("\n===== MOVIES BY GENRE =====")

    result = analyzer.movies_by_genre()

    print(result.to_string())


def show_movies_by_year(analyzer):
    print("\n===== MOVIES RELEASED PER YEAR =====")

    result = analyzer.movies_by_year()

    print(result.to_string())


def search_movie(analyzer):
    movie_name = input("\nEnter movie name: ").strip()

    if not movie_name:
        print("Movie name cannot be empty.")
        return

    result = analyzer.search_movie(movie_name)

    display_movies(result)


def filter_by_genre(analyzer):
    genre = input("\nEnter genre: ").strip()

    if not genre:
        print("Genre cannot be empty.")
        return

    result = analyzer.filter_by_genre(genre)

    display_movies(result)


def filter_by_rating(analyzer):
    try:
        rating = float(
            input("\nEnter minimum rating: ")
        )

        if rating < 0 or rating > 10:
            print("Rating must be between 0 and 10.")
            return

        result = analyzer.filter_by_rating(rating)

        display_movies(result)

    except ValueError:
        print("Please enter a valid number.")


def generate_charts(visualizer):
    print("\n===== GENERATING CHARTS =====")

    try:
        rating_chart = visualizer.rating_distribution()
        genre_chart = visualizer.genre_comparison()
        year_chart = visualizer.movies_released_per_year()

        print("\nCharts generated successfully!")

        print(f"\n1. {rating_chart}")
        print(f"2. {genre_chart}")
        print(f"3. {year_chart}")

    except Exception as error:
        print(f"\nError generating charts: {error}")


def show_menu():
    print()
    print("=" * 70)
    print("       TAMIL MOVIE RATING ANALYSIS SYSTEM")
    print("=" * 70)

    print("1.  Basic Information")
    print("2.  Rating Statistics")
    print("3.  Top 5 Highest-Rated Movies")
    print("4.  Top 5 Lowest-Rated Movies")
    print("5.  Genre-wise Average Rating")
    print("6.  Movies by Genre")
    print("7.  Movies Released Per Year")
    print("8.  Search Movie")
    print("9.  Filter Movies by Genre")
    print("10. Filter Movies by Minimum Rating")
    print("11. Generate Charts")
    print("0.  Exit")

    print("=" * 70)


def main():

    print("\nLoading movie database...")

    try:
        data_manager = MovieDataManager(DATA_FILE)

        database = data_manager.load_movies()

        analyzer = MovieAnalyzer(DATA_FILE)

        visualizer = MovieVisualizer(DATA_FILE)

        print(
            f"Successfully loaded "
            f"{database.get_movie_count()} movies."
        )

    except Exception as error:
        print(f"\nUnable to load application: {error}")
        return

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_basic_information(analyzer)

        elif choice == "2":
            show_rating_statistics(analyzer)

        elif choice == "3":
            show_highest_rated(analyzer)

        elif choice == "4":
            show_lowest_rated(analyzer)

        elif choice == "5":
            show_genre_analysis(analyzer)

        elif choice == "6":
            show_movies_by_genre(analyzer)

        elif choice == "7":
            show_movies_by_year(analyzer)

        elif choice == "8":
            search_movie(analyzer)

        elif choice == "9":
            filter_by_genre(analyzer)

        elif choice == "10":
            filter_by_rating(analyzer)

        elif choice == "11":
            generate_charts(visualizer)

        elif choice == "0":
            print("\nThank you for using Tamil Movie Rating Analysis System!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()