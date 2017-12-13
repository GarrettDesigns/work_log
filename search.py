'''Module containing the search functionality of the application'''

# Import Python standard libraries
import re
from datetime import datetime

# Import custom classes and helper methods
import constants
from menu import Menu
from utils import Utilities
from validation import Validation
from entry import Entry


class Search:
    '''This class contains all methods for searching the worklog
    and displaying the results'''

    def __init__(self):
        self.utils = Utilities()
        self.validation = Validation()
        self.entry = Entry()
        self.menu = Menu()

        self.results = list()

    def search(self, query_text, search_type=''):
        '''Method for searching the worklog

        This method takes the text to ask the user for input
        and the type of search to conduct.'''

        while True:
            self.utils.clear_screen()
            query = input(query_text).lower()

            worklog = self.utils.read_file()

            if search_type == 'date':
                if not self.validation.is_valid_date(query):
                    continue
            elif search_type == 'time_spent':
                if not self.validation.is_valid_number(query):
                    continue
            elif search_type == 'exact_match' or search_type == 'regex':
                if not self.validation.is_valid_input(query):
                    continue
            elif search_type == 'date_range':
                if not self.validation.is_valid_date_range(query.split(', ')):
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

                elif search_type == 'date_range':
                    real_date = datetime.strptime(
                        line['date'], '%m/%d/%Y')
                    date_range = query.split(', ')

                    if (datetime.strptime(date_range[0], '%m/%d/%Y') <=
                            real_date and
                            datetime.strptime(date_range[1], '%m/%d/%Y') >=
                            real_date):
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
        '''This method displays the results of a user search
        if any are found.'''

        index = 0

        while True:
            num_results = len(self.results)
            entry = self.results[index]

            self.utils.clear_screen()

            print('\n{} Search Results Found'.format(num_results))
            print("-------------------------------\n")

            print('title: {}'.format(entry['title']))
            print('date: {}'.format(entry['date']))
            print('time spent: {}'.format(entry['time_spent']))
            print('notes: {}'.format(entry['notes']))

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

            elif choice == 'e' or choice == 's' or choice == 'd':
                if choice == 'e':
                    self.entry.update_current_entry(
                        entry['id'], edit_mode='edit')
                if choice == 'd':
                    self.entry.update_current_entry(
                        entry['id'], edit_mode='delete')

                self.menu.display(constants.SEARCH_MENU)
                self.results = list()

                break
