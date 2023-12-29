import pandas as pd
from tabulate import tabulate
from typing import Union
from file import File
from movie import Movie


class Watchlist:
    """Class representing user's movie watchlist"""

    def __init__(self):
        """Initialize 'movies.csv' file"""

        self.reader = File.read_file()

    def get_watchlist(self) -> Union[str, bool]:
        """Get watchlist information in tabulated form"""

        if len(self.reader) == 0:
            return False
        include_columns = ["Title", "Genres", "Rating"]
        df = pd.DataFrame(data=self.reader,
                          columns=include_columns)
        data_for_tabulate = df.values.tolist()
        return tabulate(data_for_tabulate, headers=include_columns, showindex=True, tablefmt="psql")

    def get_movie_details(self):
        """Get details on user's chosen movie"""

        while True:
            try:
                self.index = int(input("Enter position: "))
                print()
                df = pd.DataFrame(data=self.reader)
                row = df.iloc[self.index]
                break
            except (ValueError, IndexError):
                print(
                    "Program expects position number as input (e.g. '0'). Please enter valid position.")
                continue
        movie = Movie(*row)
        print(movie.get_details())

    def delete_movie(self):
        """Delete movie and write updated information to csv file"""

        df = pd.DataFrame(data=self.reader)
        df_updated = df.drop(self.index)
        df_updated.to_csv(File.filename, index=False, header=False)
        return

    def check_if_duplicate(self, id) -> bool:
        """Method for checking if movie is already in watchlist based on ID"""

        if len(self.reader) != 0:
            df = pd.DataFrame(data=self.reader)
            if (df["ID"] == id).any():
                return True
        return False
