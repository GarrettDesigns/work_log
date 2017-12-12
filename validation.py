'''This module contains methods for validating user input'''

import datetime


class Validation:
    def is_valid_input(self, user_input, menu=''):
        if user_input == '':
            input("\nYou must enter a valid input."
                  " Press enter to try again.")
            return False
        elif user_input not in menu:
            input('\n{} is not a valid choice!'
                  ' Press enter to try again.'.format(user_input))
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
