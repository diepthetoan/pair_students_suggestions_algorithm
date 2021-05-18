import pandas as pd
import xlrd


def read_file():
    loc = 'C:\\workspace\\OneDrive - Robert Bosch GmbH\\03_Master\\01_HK1\\GiaiThuatNangCao\\pair_students_suggestions_algorithm-master\\week1.xlsx'
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    outData = []
    for i in range(2, 11):
        pointWeek = sheet.col_values(i)
    outData.append(pointWeek)
    return outData


def read_file_csv(uri):
    data = pd.read_csv(uri, skipfooter=1)
    return data
