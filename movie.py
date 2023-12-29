from termcolor import colored
from typing import Union, List
from genres import Genres
from file import File


class Movie:
    """Class representing movie object"""

    def __init__(self, genres: Union[List[int], str], id: int, title: str, overview: str, release_date: str, rating: float):
        """Initialize movie data"""

        self.genres = genres
        self.id = id
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.rating = rating

    def add_to_watchlist(self):
        """Add movie to 'movies.csv' file"""

        row = {
            "Genres": self.genres,
            "ID": self.id,
            "Title": self.title,
            "Overview": self.overview,
            "Release date": self.release_date,
            "Rating": self.rating
        }
        File.append_file(row)
        print("Movie added to watchlist")

    def get_details(self) -> str:
        """Get movie details as a formatted string"""

        formatted_output = (
            f"\n{colored(self.title, attrs=['bold'])}\n"
            f"{self.overview}\n\n"
            f"{colored('Genres: ', attrs=['bold'])}"
            f"{self.genres}\n"
            f"{colored('Release date: ', attrs=['bold'])}"
            f"{self.release_date}\n"
            f"{colored('Rating: ', attrs=['bold'])}{self.rating}\n"
        )
        return formatted_output

    @property
    def genres(self) -> Union[List[int], str]:
        """If genres are passed as IDs they are converted into a string"""

        return self._genres

    @genres.setter
    def genres(self, genres: Union[List[int], str]):
        if isinstance(genres, list):
            gen = Genres()
            genre_names = ", ".join(gen.genre_ids_to_names(genres))
            self._genres = genre_names
        else:
            self._genres = genres
