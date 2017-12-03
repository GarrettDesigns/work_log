"""The module containing methods to govern the display
   and functionality of the menu navigation system"""


class Menu:

    def __init__(self, menu):
        self.menu = menu

    def display(self):
        """Display the current menu for the worklog.

        User can select between options to search for records,
        create a new one, or quit the program entirely.
        """

        print("\nWould you like to:"
              "\n-------------------------------")

        for line in self.menu:
            print(line)

        print("-------------------------------")
