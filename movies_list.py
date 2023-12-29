import random
import re
import globals
from termcolor import colored
from typing import List
from api_call import APICall
from genres import Genres


class MoviesList:
    """Class representing movie list"""

    def __init__(self, rating):
        """Initializing movie list, rating, url and number of total pages"""

        self.movies_list = []
        self.rating = rating
        self.url = f"https://api.themoviedb.org/3/discover/movie?api_key={globals.API_KEY}&include_adult=false&include_video=false&language=en-US&sort_by=popularity.desc&vote_average.gte={self.rating}&vote_count.gte=200"
        self.total_pages = self.get_total_pages()

    def get_movie(self) -> dict:
        """Get movie from the list, if list is empty update the list"""

        if len(self.movies_list) == 0:
            self.update_movie_list()

        movie = self.movies_list[0]
        self.movies_list.pop(0)
        return movie

    def update_movie_list(self):
        """Update movie list using random page results"""

        page = random.randint(1, self.total_pages)
        url = self.url + f"&page={page}"

        movie_data = APICall.get_movie_data(url)
        self.append_movies_to_list(movie_data)

    def get_total_pages(self) -> int:
        """Get information on total number of pages from page one"""

        total_pages = APICall.get_total_no_of_pages(self.url)
        return total_pages

    def append_movies_to_list(self, movie_data: List[dict]):
        """Append movie list with 6 randomly chosen movies from a page"""

        movies_per_page = len(movie_data)
        no_of_movies_to_add = 6

        # If there is less than 6 movies in a page, append all results
        if movies_per_page <= no_of_movies_to_add:
            unique_integers = [i for i in range(0, movies_per_page)]
            random.shuffle(unique_integers)
        else:
            unique_integers = random.sample(
                range(0, movies_per_page-1), no_of_movies_to_add)

        for i in unique_integers:
            self.movies_list.append(movie_data[i])


class MoviesByGenre(MoviesList):
    """Class representing movie list that is generated based on user's chosen genres"""

    def __init__(self, rating):
        super().__init__(rating)

    def get_total_pages(self) -> int:
        """Get user's genre choices and total number of pages"""

        while True:
            try:
                self.genres = self.get_genres_parameter()
                total_pages = APICall.get_total_no_of_pages(
                    self.url + f"&with_genres={self.genres}")
                return total_pages
            except ValueError as e:
                print(e)
                continue

    def update_movie_list(self):
        """Update movie list using random page results"""

        page = random.randint(1, self.total_pages)
        url = self.url + f"&page={page}&with_genres={self.genres}"

        movie_data = APICall.get_movie_data(url)
        self.append_movies_to_list(movie_data)

    def get_user_input(self) -> List[str]:
        """Get user's genre choices"""

        names_input = input(
            "Enter genre names separated by commas (e.g. action, science fiction): ")
        if re.search(r"^(?:[a-zA-Z]|\s)+(?:,\s?(?:[a-zA-Z]|\s)+)*$", names_input):
            names = names_input.split(",")
            names_list = [name.strip().title() for name in names]
            return names_list
        else:
            raise ValueError("Invalid input")

    def get_genres_parameter(self) -> str:
        """Get a genres parameter string to add to URL for calling API"""

        genres = Genres()
        all_genres = genres.get_all_genre_names()
        all_genres_str = ", ".join(all_genres)
        print(colored("Available genres:", attrs=['bold']))
        print(all_genres_str)
        print()
        while True:
            try:
                genre_names = self.get_user_input()
                genre_ids = genres.genre_names_to_ids(genre_names)
                break
            except ValueError as e:
                print(e)
                print()
                continue

        genres_str = ""
        substring = "%2C"
        for id in genre_ids:
            genres_str += f"{id}%2C"
        genres_str = genres_str[:-len(substring)]
        return genres_str
