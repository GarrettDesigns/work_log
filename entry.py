'''Module containing the Entry class which is responsible for
  controlling all entryic and data pertaining to work entry entries'''


import datetime

from utils import Utilities


class Entry(dict):
    '''The worklog entry class contains all properties and methods
    CRUD operations, pertaining to log entries.'''

    def __init__(self):
        super().__init__()
        self.utils = Utilities()

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
            try:
                datetime.datetime.strptime(self['date'], '%m/%d/%Y')
            except ValueError:
                input("\n{} doesn't seem to be a valid date!"
                      " Press enter to try again.".format(
                          self['date']))
                self.utils.clear_screen()
                continue

            break

        while True:
            self['time_spent'] = input(
                "Please enter the time spent on this entry in hours: ")
            try:
                int(self['time_spent'])
            except ValueError:
                input("\n{} is not a valid amount of time,"
                      " please enter a number. Press enter to try again."
                      .format(self['time_spent']))

                self.utils.clear_screen()
                continue

            break

        self['notes'] = input(
            "Enter any notes about this entry (optional): ")

        return self
