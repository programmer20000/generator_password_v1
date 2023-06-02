from datetime import datetime

from .create_files import (create_text_file,create_excel_file, create_json_file,create_csv_file)

datetime_password = {}

now = datetime.now()  # current date and time
date_and_time = now.strftime("%m/%d/%Y, %H:%M:%S")


def select_variance(variance: str, password: str = ''):
    datetime_password.update({date_and_time: password})
    match variance:
        case '1':
            create_text_file(password=password)
        case '2':
            create_excel_file(dictionary=datetime_password)

        case '3':
            create_json_file(dictionary=datetime_password)
        case '4':
            create_csv_file(date_time=date_and_time,password=password)


def the_users_desire(want: str, password: str):
    match want:
        case 'y':
            select_variance(
                variance=input(
                    'Please Select Format File For Written Password [1 write in text file] [2 write in excel file] [3 '
                    'write in json file] [4 write in csv file]: '),
                password=password)
        case 'n':
            print('Goo Bay')
            exit()

        case _:
            print('variance not found')
