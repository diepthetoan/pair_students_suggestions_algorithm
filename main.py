from helper import *
from read import *


def main():
    print("Main: Start")

    # Read file CSV
    weeks = read_file()
    print('Read CSV: ', weeks)

    # Preprocessing data
    # ....
    # ...

    # Algorithm
    handle_algorithm(weeks)

    print("Main: End")

if __name__ == "__main__":
    main()