from write import *
from read import *


def get_file_name(number):
    return 'week' + str(number) + '.csv'


def format_origin_file(uri):
    week = read_file_csv(uri)
    return week.iloc[:, [0, 1, 6]]


def format_all_origin_files(path):
    class1_files = [
        './datasets/origin/Week1/CO3005_003904_DH_HK201-Quiz Introduction (T2 2892020)-dixm.csv',  # week1, class1
        './datasets/origin/Week2/CO3005_003904_DH_HK201-Quiz Lexical Analysis (T2 2892020)-dixm.csv',  # week2, class2
        './datasets/origin/Week4/CO3005_003904_DH_HK201-Quiz OOP (T2 12102020)-dixm.csv',
        './datasets/origin/Week5/CO3005_003904_DH_HK201-Quiz Functional Programming (T2)-dixm.csv',
        './datasets/origin/Week7/CO3005_003904_DH_HK201-Quiz Name, Scope and Referencing Environment (T2 16112020)-dixm.csv',
        './datasets/origin/Week8/CO3005_003904_DH_HK201-Quiz Type (T4 - Titt 012)-dixm.csv',
        './datasets/origin/Week10/CO3005_003904_DH_HK201-Quiz Sequence Control (T2 07122020)-dixm.csv',
        './datasets/origin/Week11/CO3005_003904_DH_HK201-Quiz Control Abstraction (T2 14122020)-dixm.csv',
    ]

    # TODO: Nên save các file cùng số hàng
    for i in range(0, len(class1_files)):
        # Format an origin file again
        data = format_origin_file(class1_files[i])

        # save the formatted file
        write_to_csv(data, path, get_file_name(i))
