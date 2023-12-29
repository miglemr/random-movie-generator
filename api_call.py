import requests
from typing import List


class APICall:
    """Class for making requests to movie API"""

    @classmethod
    def get_api_response(cls, url: str) -> dict:
        """Method for getting API response"""

        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @classmethod
    def get_total_no_of_pages(cls, url: str) -> int:
        """Gets information on total number of pages from the first page of movie results"""

        response = cls.get_api_response(url)
        total_pages = int(response["total_pages"])
        if total_pages == 0:
            raise ValueError("No results")
        return total_pages

    @classmethod
    def get_movie_data(cls, url: str) -> List[dict]:
        """Gets relevant movie data from response and appends it to a list"""

        movie_data = []
        response = cls.get_api_response(url)

        for i in response["results"]:
            movie = {
                "genre_ids": i["genre_ids"],
                "id": i["id"],
                "title": i["title"],
                "overview": i["overview"],
                "release_date": i["release_date"],
                "rating": i["vote_average"]
            }
            movie_data.append(movie)
        return movie_data

    @classmethod
    def get_all_genres(cls, url: str) -> List[dict]:
        """Gets all existing movie genres from the API"""

        response = cls.get_api_response(url)
        return response["genres"]
