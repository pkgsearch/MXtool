from colorama import Fore
import os
sel = input(Fore.GREEN + """[1]Дудос
[2] Бомбер
[3] Фишинг любого сайта
[4] Спамер тг
[5] Емаил бомбер
Выберите параметр: """)
if sel == "1":
    os.system("clear")
    os.system("python ~/px/core/tools/DDOS.py")
elif sel == "2":
       os.system("clear") 
       os.system("python ~/px/core/tools/BOMBER.py")
elif sel == "3":
       os.system("clear")
       os.system("python ~/px/core/tools/PKGFISH.py")
elif sel == "4":
       os.system("python ~/px/core/packages/tgspam/menutg.py")
elif sel == "5":
       os.system("python ~/px/core/packages/email/menuem.py")
else:
    print("Выбор не корректен :(\nПопробуйте еще раз!")
    exit(0)
