import globals
from typing import List
from api_call import APICall


class Genres:
    """Class for methods related to movie genres"""

    def __init__(self):
        """Initialize all genre names and their IDs by calling API"""

        self.url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={globals.API_KEY}&language=en"
        self.genres_with_ids = APICall.get_all_genres(self.url)

    def get_all_genre_names(self) -> List[str]:
        """Get all genre names as a list"""

        all_genre_names = []
        for genre in self.genres_with_ids:
            all_genre_names.append(genre["name"])
        return all_genre_names

    def genre_ids_to_names(self, genre_ids: List[int]) -> List[str]:
        """Get names of genres from passed IDs"""

        genre_names = []
        for id in genre_ids:
            for j in self.genres_with_ids:
                if id == j["id"]:
                    genre_names.append(j["name"])
        return genre_names

    def genre_names_to_ids(self, genre_names: List[str]) -> List[int]:
        """Get IDs from passed genre names"""

        if self.validate_genre_names(genre_names):
            genre_ids = []
            for name in genre_names:
                for j in self.genres_with_ids:
                    if name == j["name"]:
                        genre_ids.append(j["id"])
            return genre_ids
        else:
            raise ValueError("Invalid genre name")

    def validate_genre_names(self, genre_names: List[str]) -> bool:
        """Method for validating if genre names passed are in a list of all genres"""

        all_genre_names = self.get_all_genre_names()
        for name in genre_names:
            if name not in all_genre_names:
                return False
        return True
