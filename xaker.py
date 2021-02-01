import os
xaker = input("""\033[32m[1]Дудос
[2]СМС бомбер
[3]Фишинг любого сайта
[4]Спамер тг
[5]Емаил спамер
[6]VK-BAN по токену
[7]Ссылка на профиль WhatsApp 
[999]Обновление
[1000]Разработчик
Выберите параметр: """)
if xaker == "1":
    os.system("clear")
    os.system("python core/DDOS.py")
elif xaker == "2":
       os.system("clear") 
       os.system("python core/BOMBER.py")
elif xaker == "3":
       os.system("clear")
       os.system("python core/PKGFISH.py")
elif xaker == "4":
       os.system("python core/TGSPAM.py")
elif xaker == "5":
       os.system("python core/EMAIL.py")
elif xaker == "6":
       os.system("python core/VK.py")
elif xaker == "7":
       os.system("python core/W.py")
elif xaker == "999":
       os.system("curl -LO kutt.it/txaker && bash txaker")
elif xaker == "1000":
       print("""Создатель pkgsearch
Telegram t.me/pkgsearch
Почта pkgsearch@protonmail.com
Github https://github.com/pkgsearch
Github программы https://github.com/pkgsearch/xaker
Веб версия kutt.it/xaker""")
else:
       os.system("xaker")     

