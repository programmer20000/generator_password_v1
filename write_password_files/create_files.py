import csv
import json

import openpyxl


def create_text_file(password: str = ''):
    with open(file='yours_password.txt', mode='w') as file:
        file.write(password)


def create_json_file(dictionary: dict):
    with open(file='yours_password.json', mode='w') as file:
        json.dump(dictionary, file, indent=4)


def create_excel_file(dictionary: dict):
    book = openpyxl.Workbook()
    sheet = book.active

    sheet['A1'] = 'DATA AND TIME'
    sheet['B1'] = 'PASSWORD'
    row = 2

    for key, value in dictionary.items():
        sheet[row][0].value = key
        sheet[row][1].value = value
        row += 1

    book.save('yours_password.xlsx')


def create_csv_file(date_time: str = '', password: str = ''):
    with open(file='yours_password.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerows([
            ('DATA AND TIME', 'PASSWORD'),
            [date_time, password]
        ])
