from requests.exceptions import RequestException
from movies_list import MoviesList, MoviesByGenre
from movie import Movie
from menu import Menu
from watchlist import Watchlist

menu_error_message = "Program expects a number as input (e.g. '1'). Please enter a valid option."


def movies_mode(option: str, rating: float):
    """Function for getting movies"""

    api_call_error_message = "An error occured when calling API"

    # Construct movie list object
    if option == "Random movie":
        try:
            movie_list = MoviesList(rating)
        except RequestException:
            print(api_call_error_message)
            return
        except ValueError as e:
            print(e)
            return
    elif option == "Random movie by genre":
        try:
            movie_list = MoviesByGenre(rating)
        except RequestException:
            print(api_call_error_message)
            return

    # Get movie from a list and print its details
    while True:
        try:
            movie_info = movie_list.get_movie()
        except RequestException:
            print(api_call_error_message)
            return
        movie = Movie(*movie_info.values())
        print(movie.get_details())

        # Prompt user with menu
        while True:
            add_movie_options = ["Add to watchlist", "Skip", "Quit"]
            try:
                add_movie_menu = Menu(add_movie_options)
                add_movie_option = add_movie_menu.get_menu()
                break
            except ValueError:
                print(menu_error_message)
                continue

        # If user wants to add movie to watchlist check if it doesn't already exist and add it
        if add_movie_option == "Add to watchlist":
            id = str(movie.id)
            watchlist = Watchlist()
            if watchlist.check_if_duplicate(id):
                print("\nMovie is already in your watchlist.")
                continue
            movie.add_to_watchlist()
            continue
        elif add_movie_option == "Skip":
            continue
        elif add_movie_option == "Quit":
            return


def watchlist_mode():
    """Function for getting user's watchlist"""

    # Print user's watchlist, if empty - function returns false, in that case return to main menu
    while True:
        watchlist = Watchlist()
        movies = watchlist.get_watchlist()
        if movies:
            print(movies)
        else:
            print("Watchlist is empty\n")
            break

        # Prompt user to get more details on movie
        while True:
            try:
                watchlist_options = ["Get movie details", "Quit"]
                watchlist_menu = Menu(watchlist_options)
                option = watchlist_menu.get_menu()
                pass
            except ValueError:
                print(menu_error_message)
                continue

            # Print movie details and prompt user if they want to delete the movie
            if option == "Get movie details":
                watchlist.get_movie_details()
                while True:
                    try:
                        movie_details_options = [
                            "Delete this movie", "Back"]
                        movie_details_menu = Menu(
                            movie_details_options)
                        movie_details_option = movie_details_menu.get_menu()
                        break
                    except ValueError:
                        print(menu_error_message)
                        continue
                if movie_details_option == "Delete this movie":
                    watchlist.delete_movie()
                    print("Movie deleted\n")
                    break
                elif movie_details_option == "Back":
                    break
            elif option == "Quit":
                return
