"""The utility file for storage of common utility methods and variables"""


# import standard Python libraries
import csv

# import custom libraries and classes
import constants


class Utilities:
    '''Class containing different utility methods for the worklog.'''

    def clear_screen(self):
        '''Method providing a way to clear the screen after
          interface selections'''

        print("\033c", end="")

    def read_file(self):
        '''Method to read file contents and return them.

        This method is used to allow storing of worklog data
        as an array of dictionaries in a variable or some other
        container for use in logic.'''

        file_contents = list()

        with open('worklog.csv', 'r') as log:
            reader = csv.DictReader(
                log, fieldnames=constants.FIELDNAMES)

            next(reader)

            for line in reader:
                file_contents.append(line)

            return file_contents
