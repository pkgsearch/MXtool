from telethon import TelegramClient, events, sync
import os
from colorama import Fore, Back, Style

def cls():
    os.system('clear')

api_id = int(input(Fore.MAGENTA + " API ID с my.telegram.org: "))
api_hash = input(" API Hash с my.telegram.org: ")

client = TelegramClient('session_name', api_id, api_hash)

client.start()

cls()
      
print(Fore.CYAN + '''
███████  ▒███▒  ▓███▒ █████░   ██   █▒  ▒█
   █    ░█▒ ░█ █▓  ░█ █   ▓█   ██   ██  ██
   █    █▒     █      █    █  ▒██▒  ██░░██
   █    █      █▓░    █   ▓█  ▓▒▒▓  █▒▓▓▒█
   █    █   ██  ▓██▓  █████░  █░░█  █ ██ █
   █    █    █     ▓█ █       █  █  █ █▓ █
   █    █▒   █      █ █      ▒████▒ █    █
   █    ▒█░ ░█ █░  ▓█ █      ▓▒  ▒▓ █    █
   █     ▒███▒ ▒████░ █      █░  ░█ █    █                      
 PKGSEARCH
 
''')
      
print(Fore.GREEN + """
 [1] Бесконечный флуд 
 [2] флуд с указанным количеством сообщений 
""")


a = input(Fore.YELLOW + ' Выберите способ флуда: ')

if a == "1":
    print(" ")
    print(Fore.BLUE + " ")
    idp = input("Введите id/nick человека: ")
    mes = input("Текст сообщения ")
    print(Fore.RED + 'Спам начат! ')
    while True:

        client.send_message(idp, mes)

elif a == "2":
    print(" ")
    print(" ")  
    px = int(input(Fore.BLUE + " сообщений: "))
    idp = input("  id/nick чела: ")
    mes = input(" Текст сообщения: ")
    print(Fore.RED + '   Спам начат! ')
    for i in range(px):
        client.send_message(idp, mes)

else:
    print(" Нету такого ")
