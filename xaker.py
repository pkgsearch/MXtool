import os
xaker = input("""\033[32m[1]Дудос
[2]бомбер
[3] Фишинг любого сайта
[4] Спамер тг
Выберите параметр: """)
if xaker == "1":
    os.system("clear")
    os.system("python /core/DDOS.py")
elif xaker == "2":
       os.system("clear") 
       os.system("python /core/BOMBER.py")
elif xaker == "3":
       os.system("clear")
       os.system("python /core/PKGFISH.py")
elif xaker == "4":
       os.system("python core/TGSPAM.py")
elif xaker == "5":
       os.system("python core/EMAIL.py")
else:
    print("Выбор не корректен :(\nПопробуйте еще раз!")
    exit(0)
