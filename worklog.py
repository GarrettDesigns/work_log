"""Module contains the worklog object."""

import csv
import os

import constants
from menu import MainMenu
from search import Search


class WorkLog:
    """The worklog class representing the work log and all of its data."""

    def __init__(self):
        self.main_menu = MainMenu()
        self.search = Search()

    def access_log(self):  # Find a better name for this
        """Method to display the main worklog and allow a user interaction."""

        if not os.path.exists(constants.FILENAME):
            with open(constants.FILENAME, 'a') as file:
                fieldnames = ['date', 'title', 'time_spent', 'notes']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        self.main_menu.get_user_choice()


if __name__ == '__main__':
    WorkLog().access_log()
