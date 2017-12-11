"""The utility file for storage of common utility methods and variables"""


import csv

import constants


class Utilities:

    def clear_screen(self):
        '''Method providing a way to clear the screen after
          interface selections'''

        print("\033c", end="")

    def read_file(self):
        file_contents = list()

        with open('worklog.csv', 'r') as log:
            reader = csv.DictReader(
                log, fieldnames=constants.FIELDNAMES)

            for line in reader:
                file_contents.append(line)

            return file_contents
