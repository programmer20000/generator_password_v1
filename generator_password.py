from datetime import datetime
from os import system
from random import randint
from time import sleep

import openpyxl
from colorama import Fore

from symbols_for_password import symbols_for_password

datetime_password = {}


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


def generator_password():
    print(f'{Fore.RED}Enter count symbol for password only 1 to 2048')
    question_user = int(input(f'{Fore.GREEN}Enter count symbol for password: '))

    date_and_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def message_for_user():
        print(f'{Fore.RED} Please enter count symbol for password only 1 to 2048')
        sleep(6)
        system('cls')
        exit()

    password = ''

    if question_user > len(symbols_for_password):
        message_for_user()

    for i in range(question_user):
        password = f'{password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
        datetime_password.update({date_and_time: password})
    create_excel_file(dictionary=datetime_password)


while True:
    generator_password()
    print("if your want to exit enter (y) if not enter (n)")
    exit_from_program = input("your want to exit: ")

    if exit_from_program == "y":
        system('cls')
        break

    if exit_from_program == "n":
        system("cls")
        continue
