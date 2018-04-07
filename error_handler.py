import sys


def print_and_exit(message: str):
    print("error: " + message)
    sys.exit()


def warning(message: str):
    print(message)
