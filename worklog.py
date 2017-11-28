"""Module contains the worklog object."""


class WorkLog:
    """The worklog class representing the work log and all of its data."""

    def __init__(self):
        self.display_menu()

    def display_menu(self):
        """Display the menu for the worklog.

        User can select between options to seach for records by date,
        time spent, and exact keyword match, or regular expression.
        """
        self.choice = input("Would you like to search by [D]ate,"
                            " [T]ime Spent, [E]xact Match, or [R]egEx? ")


if __name__ == '__main__':
    WorkLog()
