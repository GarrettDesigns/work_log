"""The module containing methods to govern the display
   and functionality of the menu navigation system"""


import csv
import constants

from utils import Utilities


class Menu:

    def display(self, menu):
        """Display the current menu for the worklog.

        User can select between options to search for records,
        create a new one, or quit the program entirely.
        """

        print("\nWould you like to:"
              "\n-------------------------------")

        for line in menu:
            print(line)

        print("-------------------------------")

    def get_user_choice(self):
        return input("\nPlease make your selection: ").lower()


class MainMenu(Menu):

    def __init__(self):
        super().__init__(menu=constants.MAIN_MENU)


class SearchMenu(Menu):

    def __init__(self):
        super().__init__(menu=constants.SEARCH_MENU)
