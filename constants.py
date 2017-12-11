'''This module contains constants that are used throughout the application'''


MAIN_MENU = ["[C] Create a new entry",
             "[S] Search existing entries",
             "[Q] Quit"]

SEARCH_MENU = ["[E] Search by Exact Date",
               "[D] Search by Date Range",
               "[P] Search by Precise Match",
               "[T] Search by Time Spent",
               "[R] Search by RegEx",
               "[M] Return to the Main Menu"]

FILENAME = 'worklog.csv'

FIELDNAMES = ['date', 'title', 'time_spent', 'notes']
