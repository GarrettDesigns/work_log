'''Module containing the Entry class which is responsible for
  controlling all entryic and data pertaining to work entry entries'''


import csv

import constants

from utils import Utilities
from validation import Validation


class Entry(dict):
    '''The worklog entry class contains all properties and methods
    CRUD operations, pertaining to log entries.'''

    def __init__(self):
        super().__init__()
        self.utils = Utilities()
        self.validation = Validation()

    def create_new_entry(self):
        '''Method to create a new work entry entry.

        This method walks the user through a series of questions
        allowing them to create a single entry entry consisting of
        a date entered, a title, the time spent working and some
        optional notes if desired'''

        self['title'] = input(
            "Please choose a title for this entry: ")

        while True:
            self['date'] = input(
                "Please enter a date in the format - MM/DD/YYYY: ")

            if not self.validation.is_valid_date(self['date']):
                self.utils.clear_screen()
                continue

            break

        while True:
            self['time_spent'] = input(
                "Please enter the time spent on this entry in hours: ")

            if not self.validation.is_valid_number(self['time_spent']):
                self.utils.clear_screen()
                continue

            break

        self['notes'] = input(
            "Enter any notes about this entry (optional): ")

        with open(constants.FILENAME, 'a') as file:
            writer = csv.DictWriter(
                file, fieldnames=constants.FIELDNAMES)
            writer.writerow(self)

        self.utils.clear_screen()

        input("Entry has been added, "
              "press enter to return to the main menu")
