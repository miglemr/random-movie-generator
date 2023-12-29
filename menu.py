from typing import List


class Menu():
    """Class for creating menus"""

    def __init__(self, options: List[str]):
        """Initializing menu options that were passed"""

        self.options = options

    def print_menu(self):
        """Method for printing menu options"""

        for i in self.options:
            n = (self.options.index(i))+1
            print(n, i)
        print()

    def get_user_input(self) -> int:
        """Get user's menu choice"""

        option = int(input("Select option: "))
        if option > len(self.options):
            raise ValueError
        return option

    def get_menu(self) -> str:
        """Print menu, get user's choice and return the menu option chosen"""

        self.print_menu()
        option = self.get_user_input()

        for i in self.options:
            n = (self.options.index(i))+1
            if n == option:
                option_name = i
        return option_name
