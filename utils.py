"""The utility file for storage of common utility methods and variables"""


class Utilities:

    def __init__(self):
        self.main_menu = ["[C] Create a new entry",
                          "[S] Search existing entries",
                          "[Q] Quit"]

        self.search_menu = ["[D] Search by Date",
                            "[T] Search by Time",
                            "[E] Search by Exact Time",
                            "[R] Search by RegEx",
                            "[M] Return to the Main Menu"]

        self.filename = 'worklog.csv'

    def clear_screen(self):
        '''Method providing a way to clear the screen after
          interface selections'''

        print("\033c", end="")
