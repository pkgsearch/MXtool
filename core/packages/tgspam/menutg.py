import os
os.system("clear")      
xaker = input("""\033[32mУ вас установлены все необходимые пакеты(colorama,telethon)?
[1]Да установлены
[2]Не установлено(установить)
Выберите параметр: """)
if xaker == "1":
    os.system("clear")
    os.system("python ~/px/core/tools/TGSPAM.py")
elif xaker == "2":
       os.system("bash ~/px/core/packages/spak.sh")