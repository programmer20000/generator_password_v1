from random import randint
from colorama import Fore
from os import system
from time import sleep
from datetime import datetime
import json
from symbols_for_password import symbols_for_password



def generator_password():
    print(f'{Fore.RED}Enter count symbol for password only 1 to 2048')
    question_user = int(input(f'{Fore.GREEN}Enter count symbol for password: '))

    date_and_time = datetime.today()

    def message_for_user():
        print('error')
        sleep(6)
        system('cls')
        exit()

    password = ''

    if question_user > len(symbols_for_password):
        message_for_user()


    for i in range(question_user):
        password = f'{password}{symbols_for_password[randint(0, len(symbols_for_password) - 1)]}'
    date_created_password = {str(date_and_time): password}


    with open(file="save_password.json", mode="a") as file:
        json.dump(date_created_password, file,indent=2)


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
