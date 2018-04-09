import sys

def print_and_exit(message: str, is_test=False):
    if not is_test:
        print("\n\n-- error: " + message + "\n")
        print()
        sys.exit()
    else:
        print("failure!", end="")


def warning(message: str):
    print(message)
