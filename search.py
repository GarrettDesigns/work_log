'''Module containing the search functionality of the application'''

import csv
import re
import datetime

import constants
from utils import Utilities


class Search:

    def __init__(self):
        self.utils = Utilities()

    def search_exact_date(self):

        results = list()

        while True:
            query_date = input('Please enter a date to search: ')

            try:
                datetime.datetime.strptime(query_date, '%m/%d/%Y')
            except ValueError:
                input("\n{} doesn't seem to be a valid date!"
                      " Press enter to try again.".format(
                          query_date))
                self.utils.clear_screen()
                continue

            break

        with open('worklog.csv') as log:
            reader = csv.DictReader(log, fieldnames=constants.FIELDNAMES)

            for line in reader:
                if query_date == line['date']:
                    results.append(line)

        if results:
            index = 0
            entry = results[index]

            while True:
                self.utils.clear_screen()

                print('title: {}\n'
                      'date: {}\n'
                      'time spent: {}\n'
                      'notes: {}\n'.format(entry['title'],
                                           entry['date'],
                                           entry['time_spent'],
                                           entry['notes']))
                print("-------------------------------\n")

                choice = input(
                    "Choose an action: "
                    "[N]ext"
                    "[P]revious"
                    "[E]dit"
                    "[D]elete"
                    "[S]earch Menu: ").lower()

                if choice == 'n':
                    entry = results[index + 1]
                elif choice == 'p':
                    entry = results[index - 1]
                elif choice == 's':
                    break
        else:
            print("-------------------------------\n")
            print('No results found...')
            input('Press Enter to try again.')
