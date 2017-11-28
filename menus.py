"""The module containing methods to govern the display
   and functionality of the menu navigation system"""

import tasks
import utils


def display_main_menu():
    """Display the main menu for the worklog.

    User can select between options to search for records, create a new one, or quite the program entirely.
    """
    while True:
        utils.clear_screen()
        choice = input(
            "\nWould you like to:"
            "\n-------------------------------"
            "\n[C] Create a new entry"
            "\n[S] Search existing entries"
            "\n[Q] Quit"
            "\n-------------------------------"
            "\nPlease make your selection: ").lower()

        if choice == 'c':
            tasks.create_new_entry()
            break
        elif choice == 's':
            utils.clear_screen()
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
            "\nWould you like to:"
            "\n-------------------------------"
            "\n[D] Search by Date"
            "\n[T] Search by Time Spent"
            "\n[E] Search by Exact Match"
            "\n[R] Search by RegEx"
            "\n[M] Return to Main Menu?"
            "\n-------------------------------"
            "\nPlease make your selection: ").lower()

        if search == 'm':
            utils.clear_screen()
            display_main_menu()
            break
