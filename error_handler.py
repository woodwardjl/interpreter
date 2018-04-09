import sys

def print_and_exit(message: str, is_test=False):
    if not is_test:
        print("-- error: " + message + "\n")
        print()
        sys.exit()
    else:
        print("failure!")


def warning(message: str):
    print(message)
