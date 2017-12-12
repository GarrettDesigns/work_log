"""Module contains the worklog object."""

import csv
import os

import constants

from utils import Utilities
from menu import Menu
from entry import Entry
from search import Search
from validation import Validation


class WorkLog:
    """The worklog class representing the work log and all of its data."""

    def access_log(self):

        menu = Menu()
        entry = Entry()
        utils = Utilities()
        search = Search()
        validation = Validation()
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

                if not validation.is_valid_input(choice, menu='csq'):
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

                elif choice == 's':
                    current_menu = constants.SEARCH_MENU

                elif choice == 'q':
                    break

            elif current_menu == constants.SEARCH_MENU:

                if not validation.is_valid_input(choice, menu='edtprm'):
                    continue

                if choice == 'e':
                    search.search('Please enter a date to search: ', 'date')

                elif choice == 'd':
                    search.search(
                        'Please enter two comma separated dates to search'
                        '\n(ex. 01/15/1982, 12/11/2017): ', 'date_range')

                elif choice == 't':
                    search.search(
                        'Please enter a time to search: ', 'time_spent')

                elif choice == 'p':
                    search.search(
                        'Please enter a word or phrase to search: ',
                        'exact_match')

                elif choice == 'r':
                    search.search(
                        'Please enter a word or phrase to search: ', 'regex')

                elif choice == 'm':
                    current_menu = constants.MAIN_MENU


if __name__ == '__main__':
    WorkLog().access_log()
