"""Module contains the worklog object."""

import csv
import os

from menu import Menu
from utils import Utilities


class WorkLog:
    """The worklog class representing the work log and all of its data."""

    def __init__(self):

        self.utils = Utilities()
        self.main_menu = Menu(menu=self.utils.main_menu)
        self.search_menu = Menu(menu=self.utils.search_menu)

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

        with open(self.utils.filename, 'a') as file:
            fieldnames = ['date', 'title', 'time_spent', 'notes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(log)

        input("Entry has been added, press enter to return to the main menu")

    def access_log(self):  # Find a better name for this
        """Method to display the main worklog and allow a user interaction."""

        if not os.path.exists(self.utils.filename):
            with open(self.utils.filename, 'a') as file:
                fieldnames = ['date', 'title', 'time_spent', 'notes']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        while True:
            self.utils.clear_screen()
            self.main_menu.display()

            choice = input("\nPlease make your selection: ").lower()

            if choice == 'c':
                self.create_new_entry()
            elif choice == 's':
                self.search_menu.display()
            elif choice == 'q':
                break


if __name__ == '__main__':
    WorkLog().access_log()
