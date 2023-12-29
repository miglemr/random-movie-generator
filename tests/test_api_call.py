import pytest
import unittest
from unittest.mock import patch, MagicMock
from api_call import APICall


class TestAPICallClass(unittest.TestCase):
    @patch("requests.get")
    def test_get_total_no_of_pages_correct(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = mock_movie_data
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        assert APICall.get_total_no_of_pages("url") == 77

    @patch("requests.get")
    def test_get_total_no_of_pages_zero(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = mock_movie_data_zero
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        with pytest.raises(ValueError):
            APICall.get_total_no_of_pages("url")

    @patch("requests.get")
    def test_get_movie_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = mock_movie_data
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        assert APICall.get_movie_data("url") == [
            {
                "genre_ids": [
                    16,
                    35,
                    10751,
                    14,
                    10749
                ],
                "id": 976573,
                "title": "Elemental",
                "overview": "In a city where fire, water, land and air residents live together, a fiery young woman and a go-with-the-flow guy will discover something elemental: how much they have in common.",
                "release_date": "2023-06-14",
                "rating": 7.8
            },
            {
                "genre_ids": [
                    16,
                    28,
                    12
                ],
                "id": 569094,
                "title": "Spider-Man: Across the Spider-Verse",
                "overview": "After reuniting with Gwen Stacy, Brooklyn\u2019s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse\u2019s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.",
                "release_date": "2023-05-31",
                "rating": 8.4
            }
        ]


mock_movie_data = {
    "page": 1,
    "results": [
        {
            "genre_ids": [
                16,
                35,
                10751,
                14,
                10749
            ],
            "id": 976573,
            "original_language": "en",
            "overview": "In a city where fire, water, land and air residents live together, a fiery young woman and a go-with-the-flow guy will discover something elemental: how much they have in common.",
            "release_date": "2023-06-14",
            "title": "Elemental",
            "vote_average": 7.8,
            "vote_count": 1553
        },
        {
            "genre_ids": [
                16,
                28,
                12
            ],
            "id": 569094,
            "original_language": "en",
            "overview": "After reuniting with Gwen Stacy, Brooklyn\u2019s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse\u2019s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.",
            "release_date": "2023-05-31",
            "title": "Spider-Man: Across the Spider-Verse",
            "vote_average": 8.4,
            "vote_count": 3855
        },
    ],
    "total_pages": 77,
    "total_results": 1523
}

mock_movie_data_zero = {
    "page": 1,
    "results": [
    ],
    "total_pages": 0,
    "total_results": 0
}

if __name__ == "__main__":
    unittest.main()
