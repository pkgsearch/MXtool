import os
xaker = input("""\033[32m[1]Дудос
[2]бомбер
[3] Фишинг любого сайта
[4] Спамер тг
[5] Емаил бомбер
Выберите параметр: """)
if xaker == "1":
    os.system("clear")
    os.system("python ~/px/core/tools/DDOS.py")
elif xaker == "2":
       os.system("clear") 
       os.system("python ~/px/core/tools/BOMBER.py")
elif xaker == "3":
       os.system("clear")
       os.system("python ~/px/core/tools/PKGFISH.py")
elif xaker == "4":
       os.system("python ~/px/core/packages/tgspam/menutg.py")
elif xaker == "5":
       os.system("python ~/px/core/packages/email/EMAIL.py")
else:
    print("Выбор не корректен :(\nПопробуйте еще раз!")
    exit(0)
    
