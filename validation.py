'''This module contains methods for validating user input'''

import datetime


class Validation:
    def is_valid_input(self, query):
        try:
            len(query)
        except ValueError:
            input("\nYou must enter a valid input."
                  " Press enter to try again.")
            return False

        return True

    def is_valid_date(self, date):
        try:
            datetime.datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            input("\n{} doesn't seem to be a valid date!"
                  " Press enter to try again.".format(
                      date))
            return False

        return True

    def is_valid_number(self, number):
        try:
            int(number)
        except ValueError:
            input("\n{} doesn't seem to be a valid number!"
                  " Press enter to try again.".format(
                      number))
            return False

        return True
