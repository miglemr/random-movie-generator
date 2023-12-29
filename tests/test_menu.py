import unittest
from unittest.mock import patch
import pytest
from menu import Menu


class TestMenuClass(unittest.TestCase):
    def setUp(self) -> None:
        self.menu = Menu([
            "First option",
            "Second option",
            "Third option"
        ])

    @patch("builtins.input", side_effect=["2"])
    def test_get_user_input_valid(self, mock_input):
        assert self.menu.get_user_input() == 2

    @patch("builtins.input", side_effect=["5"])
    def test_get_user_input_invalid(self, mock_input):
        with pytest.raises(ValueError):
            self.menu.get_user_input()

    @patch("builtins.input", side_effect=["2"])
    def test_get_menu(self, mock_input):
        assert self.menu.get_menu() == "Second option"


if __name__ == "__main__":
    unittest.main()
