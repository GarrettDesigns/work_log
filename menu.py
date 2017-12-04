"""The module containing methods to govern the display
   and functionality of the menu navigation system"""


import csv
import constants

from utils import Utilities


class Menu:

    def __init__(self, menu):
        self.menu = menu
        self.utils = Utilities()

    def display(self):
        """Display the current menu for the worklog.

        User can select between options to search for records,
        create a new one, or quit the program entirely.
        """

        print("\nWould you like to:"
              "\n-------------------------------")

        for line in self.menu:
            print(line)

        print("-------------------------------")


class MainMenu(Menu):

    def __init__(self):
        super().__init__(menu=constants.MAIN_MENU)

    def create_new_entry(self):
        '''Method to create a new work log entry.

        This method walks the user through a series of questions
        allowing them to create a single log entry consisting of
        a date entered, a title, the time spent working and some
        optional notes if desired'''

        self.utils.clear_screen()

        log = dict()

        log['date'] = input(
            "Please enter a date in the format - MM/DD/YYYY: ")
        log['title'] = input("Please choose a title for this entry: ")
        log['time_spent'] = input(
            "Please enter the time spent on this entry: ")
        log['notes'] = input(
            "Enter any notes about this entry (optional): ")

        self.utils.clear_screen()

        with open(constants.FILENAME, 'a') as file:
            fieldnames = ['date', 'title', 'time_spent', 'notes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(log)

        input("Entry has been added, press enter to return to the main menu")

    def get_user_choice(self):
        while True:
            self.utils.clear_screen()
            self.display()

            choice = input("\nPlease make your selection: ").lower()

            if choice == 'c':
                self.create_new_entry()
            elif choice == 's':
                SearchMenu().get_user_choice()
                break
            elif choice == 'q':
                break


class SearchMenu(Menu):

    def __init__(self):
        super().__init__(menu=constants.SEARCH_MENU)

    def get_user_choice(self):
        while True:
            self.utils.clear_screen()
            self.display()

            choice = input("\nPlease make your selection: ").lower()

            if choice == 'm':
                MainMenu().get_user_choice()
                break
