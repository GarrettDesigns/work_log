"""Module containing all methods and variables related to worklog tasks

This modules defines methods which execute various operations on log entries
such as creating, updating or deleting them"""

import utils
import menus


def create_new_entry():
    '''Method to create a new work log entry.

    This method walks the user through a series of questions
    allowing them to create a single log entry consisting of
    a date entered, a title, the time spent working and some
    optional notes if desired'''

    utils.clear_screen()

    log = dict()
    log['date'] = input("Please enter a date in the format - MM/DD/YYYY: ")
    log['title'] = input("Please choose a title for this entry: ")
    log['time_spent'] = input("Please enter the time spent on this entry: ")
    log['notes'] = input("Enter any notes about this entry (optional): ")

    utils.clear_screen()

    input("Entry has been added, press enter to return to the main menu")
    menus.display_main_menu()
