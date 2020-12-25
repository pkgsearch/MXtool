import os
os.system("clear")      
xaker = input("""\033[32mУ вас установлены все необходимые пакеты(colorama,smtlib)?
[1]Да установлены
[2]Не установлено(установить)
Выберите параметр: """)
if xaker == "1":
    os.system("clear")
    os.system("python ~/px/core/tools/EMAIL.py")
elif xaker == "2":
       os.system("bash ~/px/core/packages/empak.sh")
