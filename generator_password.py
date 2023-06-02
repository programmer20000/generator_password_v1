from os import system
from random import randint
from time import sleep

from colorama import Fore

from symbols_for_password import symbols_for_password
from write_password_files import the_users_desire


def generator_password():
    print(f'{Fore.RED}Enter count symbol for password only 1 to 2048')
    question_user = int(input(f'{Fore.GREEN}Enter count symbol for password: '))

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
    print(password)
    the_users_desire(want=input('want do yours write paasword in file (y) or (n): \n'), password=password)


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
