'''This module contains methods for validating user input'''

import datetime


class Validation:

    def is_valid_date(self, date):
        try:
            datetime.datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            input("\n{} doesn't seem to be a valid date!"
                  " Press enter to try again.".format(
                      date))
            return False

        return True
