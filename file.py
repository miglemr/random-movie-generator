import csv
from typing import List
import globals


class File:
    """Class for methods related to 'movies.csv' file"""

    filename = globals.FILENAME
    fieldnames = [
        "Genres",
        "ID",
        "Title",
        "Overview",
        "Release date",
        "Rating"
    ]

    @classmethod
    def append_file(cls, row: dict):
        """Appends file"""

        with open(cls.filename, "a") as file:
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)
            writer.writerow(row)

    @classmethod
    def read_file(cls) -> List[dict]:
        """Reads file"""

        with open(cls.filename) as file:
            reader = csv.DictReader(file, fieldnames=cls.fieldnames)
            return list(reader)
