'''Module containing the search functionality of the application'''

import csv
import re
import datetime

import constants
from utils import Utilities


class Search:

    def __init__(self):
        self.utils = Utilities()
        self.results = list()

    def search_exact_date(self):

        while True:

            self.utils.clear_screen()
            query_date = input('Please enter a date to search: ')

            try:
                datetime.datetime.strptime(query_date, '%m/%d/%Y')
            except ValueError:
                input("\n{} doesn't seem to be a valid date!"
                      " Press enter to try again.".format(
                          query_date))
                self.utils.clear_screen()
                continue

            with open('worklog.csv') as log:
                reader = csv.DictReader(
                    log, fieldnames=constants.FIELDNAMES)

                for line in reader:
                    if query_date == line['date']:
                        self.results.append(line)

            if not self.results:
                print("-------------------------------\n")
                print('No results found...')
                input('Press Enter to try again.')
                continue
            else:
                self.display_search_results()
                break

    def display_search_results(self):

        index = 0

        while True:
            entry = self.results[index]

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
                if index != (len(self.results) - 1):
                    index += 1
                else:
                    index = 0
            elif choice == 'p':
                if index != 0:
                    index -= 1
                else:
                    index = (len(self.results) - 1)
            elif choice == 's':
                break
