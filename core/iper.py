import os
import requests
import subprocess
import re
import multiprocessing
print("""
███    █▓██    ███    █▒██▒
   █    █▓ ▓█  ▓▓ ▒█   ██  █
   █    █   █  █   █   █
   █    █   █  █████   █
   █    █   █  █       █
   █    █▓ ▓█  ▓▓  █   █
 █████  █▓██    ███▒   █
        █
        █
        █
""")
try:

    domain = input('Введите домен »»»')
except KeyboardInterrupt:
    print('\nIPER закрыт !! ')
    quit()
def checker(domain):

    try:

        link=requests.get('http://'+domain)
        if link.status_code ==200 or link.status_code==403:


            ping_command = subprocess.check_output('ping -c 1 '+domain,shell=True)
            filtered_re = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ping_command.decode('utf-8'))
            print('\x1b[1;32;40m'Домен: '+domain+' Имеет айпи : '+filtered_re[0]+ '\033[0m')

        else:

            print('\x1b[0;31;40m'Домен : '+domain+' Имеет айпи: N/A '+ '\033[0m')
    except Exception:
        print('\x1b[0;31;40m'Домен : '+domain+' Имеет айпи: N/A '+ '\033[0m')
        pass
try:

    with open('iper.txt','r')as wordlist:
        for word in wordlist:
            word = word.strip()

            try:

                subwdom= word+'.'+domain
                p= multiprocessing.Process(target=checker,args=(subwdom,))
                p.start()
                p.join()
            except Exception:
                quit()
except KeyboardInterrupt:

    print('IPER закрыт!! ')
    quit()
print('IPER закрыт !! ')
