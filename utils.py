"""The utility file for storage of common utility methods and variables"""


def display_main_menu():
    """Display the menu for the worklog.

    User can select between options to search for records or create a new one.
    """
    while True:
        choice = input(
            "\n[C]reate a new entry\n[S]earch existing entries\n[Q]uit\n------"
            "-------------------------\nPlease make your selection: ").lower()

        if choice == 's':
            display_search_menu()
            break
        elif choice == 'q':
            break


def display_search_menu():
    """Display the search submenu for the worklog.

    User can select between options to search for records by date,
    time spent, and exact keyword match, regular expression or return
    to the main menu.
    """
    while True:
        search = input(
            "Would you like to search by\n[D]ate\n[T]ime Spent\n[E]xact Match"
            "\n[R]egEx\nor select [M]ain Menu? ").lower()

        if search == 'm':
            display_main_menu()
            break
