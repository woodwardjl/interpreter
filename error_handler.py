import sys

def print_and_exit(message: str, is_test=False):
    if not is_test:
        print("-- error: " + message)
        sys.exit()
    else:
        print("failure!", end="")


def warning(message: str):
    print(message)
