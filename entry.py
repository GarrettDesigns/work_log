'''Module containing the Entry class which is responsible for
  controlling all logic and data pertaining to work log entries'''

import csv

import constants
from utils import Utilities


class Entry:

    def create_new_entry(self):
        '''Method to create a new work log entry.

        This method walks the user through a series of questions
        allowing them to create a single log entry consisting of
        a date entered, a title, the time spent working and some
        optional notes if desired'''

        utils = Utilities()

        utils.clear_screen()

        log = dict()

        log['date'] = input(
            "Please enter a date in the format - MM/DD/YYYY: ")
        log['title'] = input("Please choose a title for this entry: ")
        log['time_spent'] = input(
            "Please enter the time spent on this entry: ")
        log['notes'] = input(
            "Enter any notes about this entry (optional): ")

        utils.clear_screen()

        with open(constants.FILENAME, 'a') as file:
            fieldnames = ['date', 'title', 'time_spent', 'notes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(log)

        input("Entry has been added, press enter to return to the main menu")
