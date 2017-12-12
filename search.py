'''Module containing the search functionality of the application'''

import re

import constants

from menu import Menu
from utils import Utilities
from validation import Validation


class Search:

    def __init__(self):
        self.utils = Utilities()
        self.validation = Validation()
        self.results = list()

    def search(self, query_text, search_type=''):

        while True:
            self.utils.clear_screen()
            query = input(query_text).lower()

            worklog = self.utils.read_file()

            # if not self.validation.is_valid_input(query):
            #     self.utils.clear_screen()
            #     continue

            if search_type == 'date':
                if not self.validation.is_valid_date(query):
                    self.utils.clear_screen()
                    continue

            elif search_type == 'time_spent':
                if not self.validation.is_valid_number(query):
                    self.utils.clear_screen()
                    continue

            search = re.compile(r'{}'.format(query), re.I)

            for line in worklog:
                if search_type == 'date' or search_type == 'time_spent':
                    if search.match(line[search_type]):
                        self.results.append(line)

                elif search_type == 'exact_match' or search_type == 'regex':
                    if search.findall(line['title']) \
                            or search.findall(line['notes']):
                        self.results.append(line)

            self.display_search_results()
            break

    def display_search_results(self):

        index = 0

        while True:
            if not self.results:
                print("-------------------------------\n")
                print('No results found...')
                input('Press Enter to try again.')
                break
            else:
                num_results = len(self.results)
                entry = self.results[index]

                self.utils.clear_screen()

                print('\n{} Search Results Found'.format(num_results))
                print("-------------------------------\n")
                print('title: {}\n'
                      'date: {}\n'
                      'time spent: {}\n'
                      'notes: {}\n'.format(entry['title'],
                                           entry['date'],
                                           entry['time_spent'],
                                           entry['notes']))
                print("-------------------------------")
                print('Result {}/{}'.format((index + 1), num_results))
                print("-------------------------------\n")

                choice = input(
                    "Choose an action: "
                    "[N]ext, "
                    "[P]revious, "
                    "[E]dit, "
                    "[D]elete, "
                    "[S]earch Menu: ").lower()

                if not self.validation.is_valid_input(choice, menu='npeds'):
                    self.utils.clear_screen()
                    continue

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
                    Menu().display(constants.SEARCH_MENU)
                    self.results = list()
                    break
