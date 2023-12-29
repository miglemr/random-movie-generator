import unittest
from unittest.mock import MagicMock
from genres import Genres


class TestGenresClass(unittest.TestCase):
    def setUp(self):
        self.genres = Genres()
        self.genres.get_all_genre_names = MagicMock(return_value=[
                                                    "Animation", "Action", "Comedy", "Drama", "Science fiction", "Family", "Fantasy", "Romance"])
        self.genre_with_ids = [{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 16, 'name': 'Animation'}, {
            'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}]

    def test_validate_genre_names(self):
        assert self.genres.validate_genre_names([
            "Comedy", "Family"
        ]) == True
        assert self.genres.validate_genre_names([
            "Animation comedy", "Science"
        ]) == False

    def test_genre_names_to_ids_correct(self):
        self.genres.validate_genre_names = MagicMock(return_value=True)

        assert self.genres.genre_names_to_ids([
            "Crime", "Documentary", "Drama"
        ]) == [80, 99, 18]


if __name__ == "__main__":
    unittest.main()
