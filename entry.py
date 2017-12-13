'''Module containing the Entry class which is responsible for
  controlling all entryic and data pertaining to work entry entries'''


import csv
import random

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

    def _display_keep_current_value(self, value):
        self.utils.clear_screen()
        print('Press enter to keep current value: {}'.format(
            value))
        print('-----------------')

    def _get_entry_data(self, editing=False, log_to_edit=None):

        if not editing:
            self['id'] = ''.join(random.choice(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(20))
        else:
            self['id'] = log_to_edit['id']

        current_title = " ({})".format(log_to_edit['title']) if editing else ''
        current_date = " ({})".format(log_to_edit['date']) if editing else ''
        current_time_spent = " ({})".format(
            log_to_edit['time_spent']) if editing else ''
        current_notes = " ({})".format(log_to_edit['notes']) if editing else ''

        self['title'] = input(
            "\nPlease choose a title for this entry{}: "
            .format(current_title)) or log_to_edit['title']

        while True:
            self['date'] = (input(
                "\nPlease enter a date (ex. MM/DD/YYYY){}: "
                .format(current_date)) or log_to_edit['date'])

            if not self.validation.is_valid_date(self['date']):
                self.utils.clear_screen()
                continue

            break

        while True:
            self['time_spent'] = (input(
                "\nPlease enter the time spent on this entry in hours{}: "
                .format(current_time_spent)) or log_to_edit['time_spent'])

            if not self.validation.is_valid_number(self['time_spent']):
                self.utils.clear_screen()
                continue

            break

        self['notes'] = (input(
            "\nEnter any notes about this entry (optional){}: "
            .format(current_notes)) or log_to_edit['notes'])

    def create_new_entry(self):
        '''Method to create a new work entry.

        This method walks the user through a series of questions
        allowing them to create a single entry consisting of
        a date entered, a title, the time spent working and some
        optional notes if desired'''

        self._get_entry_data()

        with open(constants.FILENAME, 'a') as file:
            writer = csv.DictWriter(
                file, fieldnames=constants.FIELDNAMES)
            writer.writerow(self)

        self.utils.clear_screen()

        input("\nEntry has been added, "
              "press enter to return to the main menu")

    def update_current_entry(self, entry_id, edit_mode):

        worklog = self.utils.read_file()
        status = 'updated' if edit_mode == 'edit' else 'deleted'

        for index, entry in enumerate(worklog):
            if entry['id'] == entry_id:
                if edit_mode == 'edit':
                    self._get_entry_data(editing=True, log_to_edit=entry)
                    worklog[index] = self

                if edit_mode == 'delete':
                    del worklog[index]

            with open('worklog.csv', 'w') as log:
                writer = csv.DictWriter(log, constants.FIELDNAMES)
                writer.writeheader()

                for row in worklog:
                    writer.writerow(row)

        self.utils.clear_screen()
        input("\nEntry has been {}! Press enter to continue.".format(status))
