'''This module contains methods for validating user input'''

import datetime


class Validation:
    '''Class containing methods to validate user input.'''

    def is_valid_input(self, user_input, menu=''):
        '''This method validates user input.

        The purpose of this method is to validate generic user
        input. i.e input that can be of any type such as numbers, strings,
        regular expressions, etc. It simply checks if there is an input.

        Additionally, it is used to check whether a user made a valid choice
        from one of the menus of the program.'''

        if user_input == '':
            input("\nYou must enter a valid input."
                  " Press enter to try again.")
            return False

        if menu != '' and user_input not in menu:
            input('\n{} is not a valid choice!'
                  ' Press enter to try again.'.format(user_input))
            return False

        return True

    def is_valid_date(self, date):
        '''This method simply validates a date format.

        It makes sure that the user entered a date and that
        it is in the format mm/dd/yyyy'''

        try:
            datetime.datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            input("\n{} doesn't seem to be a valid date!"
                  " Press enter to try again.".format(
                      date))
            return False

        return True

    def is_valid_number(self, number):
        '''This method validates an integer or a string that
        can be turned into one was entered.'''

        try:
            int(number)
        except ValueError:
            input("\n{} doesn't seem to be a valid number!"
                  " Press enter to try again.".format(
                      number))
            return False

        return True

    def is_valid_date_range(self, date_range):
        '''This is a method to valid that a user entered a range of dates.

        It checks to see that two dates were entere and makes use of this
        classes own is_valid_date() method to verify that both of them are
        actual dates in the appropriate format.'''

        if len(date_range) != 2:
            input('{}, not a valid date range.'
                  'You must enter two valid dates.'.format(''.join(date_range)))
            return False

        if not (self.is_valid_date(date_range[0])
                and self.is_valid_date(date_range[1])):
            return False

        return True
