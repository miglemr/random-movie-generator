import sys
from rating import get_rating
from modes import movies_mode, watchlist_mode
from menu import Menu


def main():
    rating = get_rating()
    main_menu_options = [
        "Random movie",
        "Random movie by genre",
        "Your movie watchlist",
        "Quit"
    ]

    while True:
        try:
            main_menu = Menu(main_menu_options)
            option = main_menu.get_menu()
            pass
        except ValueError:
            print(
                "Program expects a number as input (e.g. '1'). Please enter a valid option.")
            continue

        if option == "Random movie" or option == "Random movie by genre":
            movies_mode(option, rating)
        elif option == "Your movie watchlist":
            watchlist_mode()
        elif option == "Quit":
            sys.exit("Program quit")


if __name__ == "__main__":
    main()
