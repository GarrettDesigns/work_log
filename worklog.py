"""Module contains the worklog object."""

import csv
import os

import constants

from utils import Utilities
from menu import Menu
from entry import Entry
from search import Search


class WorkLog:
    """The worklog class representing the work log and all of its data."""

    def access_log(self):

        menu = Menu()
        entry = Entry()
        utils = Utilities()
        search = Search()
        current_menu = constants.MAIN_MENU

        if not os.path.exists(constants.FILENAME):
            with open(constants.FILENAME, 'a') as file:
                writer = csv.DictWriter(file, fieldnames=constants.FIELDNAMES)
                writer.writeheader()

        while True:
            utils.clear_screen()
            menu.display(current_menu)
            choice = menu.get_user_choice()

            if current_menu == constants.MAIN_MENU:

                if choice not in 'csq':
                    input(
                        '\n{} is not a valid choice!'
                        ' Press enter to try again.'.format(choice))
                    continue

                if choice == 'c':

                    utils.clear_screen()

                    with open(constants.FILENAME, 'a') as file:
                        writer = csv.DictWriter(
                            file, fieldnames=constants.FIELDNAMES)
                        writer.writerow(entry.create_new_entry())
                    utils.clear_screen()

                    input("Entry has been added, "
                          "press enter to return to the main menu")

                if choice == 's':
                    current_menu = constants.SEARCH_MENU
                elif choice == 'q':
                    break

            if current_menu == constants.SEARCH_MENU:
                if choice == 'e':
                    search.search_exact_date()
                if choice == 'm':
                    current_menu = constants.MAIN_MENU


if __name__ == '__main__':
    WorkLog().access_log()
