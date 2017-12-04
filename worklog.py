"""Module contains the worklog object."""

import csv
import os

import constants
from utils import Utilities
from menu import Menu
from entry import Entry


class WorkLog:
    """The worklog class representing the work log and all of its data."""

    def __init__(self):

        menu = Menu()
        entry = Entry()
        utils = Utilities()
        current_menu = constants.MAIN_MENU

        if not os.path.exists(constants.FILENAME):
            with open(constants.FILENAME, 'a') as file:
                fieldnames = ['date', 'title', 'time_spent', 'notes']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        while True:
            utils.clear_screen()
            menu.display(current_menu)
            choice = menu.get_user_choice()

            if current_menu == constants.MAIN_MENU:
                if choice == 'c':
                    entry.create_new_entry()
                if choice == 's':
                    current_menu = constants.SEARCH_MENU
                elif choice == 'q':
                    break

            if current_menu == constants.SEARCH_MENU:
                if choice == 'm':
                    current_menu = constants.MAIN_MENU


if __name__ == '__main__':
    WorkLog()
