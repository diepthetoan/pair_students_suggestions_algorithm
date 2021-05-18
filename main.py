from helper import *
from file import *

import os

# Directory
DIRECTORY = 'edited'

# Parent Directory path
PARENT_DIR = './datasets/'


def preprocessing_datasets(path):
    out_data = []
    for i in range(0, 8):
        data = read_file_csv(path + '/' + get_file_name(i))
        print('Week' + str(i) + ':', data)

    # TODO: return [[],[],[],[]]
    # return out_data
    return [
        [8.83, 7, 6.33, 9.67, 6.83, 9.67],
        [5.5, 6.56, 6.67, 4.17, 3.33, 8.22],
        [2.05, 5, 7.69, 5, 5.9, 6.67],
        [10, 8.33, 8.33, 9, 5.5, 8]
    ]


def main():
    print("Main: Start")

    # Path
    path = os.path.join(PARENT_DIR, DIRECTORY)

    # handle origin datasets
    # should run this function in the first time
    format_all_origin_files(path) # TODO: @Quy

    # Read the edited files
    weeks = preprocessing_datasets(path) # TODO: @The Anh
    print('Read CSV: ', weeks)

    #
    # # Algorithm
    handle_algorithm(weeks)

    print("Main: End")


if __name__ == "__main__":
    main()
