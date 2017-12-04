"""The utility file for storage of common utility methods and variables"""


class Utilities:

    def clear_screen(self):
        '''Method providing a way to clear the screen after
          interface selections'''

        print("\033c", end="")
