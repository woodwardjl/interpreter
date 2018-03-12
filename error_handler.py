import sys

class ErrorHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def print_and_exit(message: str):
        print("error: " + message)
        sys.exit()