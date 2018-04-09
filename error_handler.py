import sys

def print_and_exit(message: str, start_message=""):
    print("\n-- error: " + message + "\n")
    sys.exit()


def warning(message: str):
    print(message)
