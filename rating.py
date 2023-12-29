import argparse
import sys


def get_rating() -> float:
    """Get rating from command line"""

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-r",
            default=7.5,
            help="Enter minimum rating for movies. Default value is 7.5"
        )
        args = parser.parse_args()
        rating = float(args.r)
        if 1.0 > rating or rating > 10.0:
            raise ValueError
        return rating
    except ValueError:
        sys.exit(
            "Invalid command line argument. Please enter a valid rating (e.g. '7.8')")
