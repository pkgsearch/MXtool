import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
os.system("clear")
print("""\033[35m
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶111111111¶¶¶¶¶¶11111111111¶¶¶¶¶¶¶¶¶111111111¶¶¶¶
¶11111111111¶¶¶¶¶11111111111¶¶¶¶¶¶¶¶11111111111¶¶¶
¶¶1111111111¶¶¶¶¶¶¶111111111¶¶¶¶¶¶¶11111111111¶¶¶¶
¶¶¶1111111111¶¶¶¶¶¶111111111¶¶¶¶¶¶11111111111¶¶¶¶¶
¶¶¶¶1111111111¶¶¶¶¶111111111¶¶¶¶¶11111111111¶¶¶¶¶¶
¶¶¶¶¶1111111111¶¶¶¶111111111¶¶¶¶11111111111¶¶¶¶¶¶¶
¶¶¶¶¶¶11111111111¶¶111111111¶¶¶1111111111¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶111111111111111111111111111111111¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶11111111111111111111111111111111¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶11111111111111111111111111111111¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶111111111111111111111111111111111¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶11111111111111111111111111111111¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111111¶¶¶11111111111111¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111¶¶¶¶¶¶1111111111111¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111¶¶¶¶¶¶¶¶11111111111¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
█░  ░█ █   ▒▓        █████░   ██   ██   █
 ▓▒  ▒▓ █  ▒█         █   ▒█   ██   ██░  █
 ▒█  █▒ █ ▒█          █    █  ▒██▒  █▒▓  █
  █  █  █▒█           █   ▒█  ▓▒▒▓  █ █  █
  █░░█  ███░          █████░  █░░█  █ ▓▓ █
  ▓▒▒▓  █ ▒█    ███   █   ▒█  █  █  █  █ █
  ▒██▒  █  █▓         █    █ ▒████▒ █  ▓▒█
   ██   █   █░        █   ▒█ ▓▒  ▒▓ █  ░██
   ██   █   ▒█        █████░ █░  ░█ █   ██
 made by pkgsearch
""")
huy = input("Ввeди токен:") 
token = vk_api.VkApi(token = tok) 
vk = token.get_api()
vk.wall.post(message='Аккаунт  взломан! Ответственность взял анонимный хакер')
vk.wall.post(message='vto.pe')             
print("[log] Сообщение отправленно. Ожидайте бана!")

           
    
