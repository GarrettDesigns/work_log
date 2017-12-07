"""The module containing methods to govern the display
   and functionality of the menu navigation system"""


class Menu:
    '''Class to create new menu's for the application.

    Call this class passing in a list of menu choices.'''

    def display(self, menu):
        """Display the current menu for the worklog.

        User can select between options to search for records,
        create a new one, or quit the program entirely.
        """

        print("\nWould you like to:"
              "\n-------------------------------")

        for line in menu:
            print(line)

        print("-------------------------------")

    def get_user_choice(self):
        return input("\nPlease make your selection: ").lower()
