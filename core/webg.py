import os

print(
    """\033[33m

███████████████████████████████████████████████████████████████████████
█▒▒▒▒▒▒██████████▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▄▀▒▒██████████▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒███▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▄▀▒▒██████████▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▒▒▒▒▒▒▒▒▒▒█
█▒▒▄▀▒▒██████████▒▒▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒██▒▒▄▀▒▒███▒▒▄▀▒▒█████████
█▒▒▄▀▒▒██▒▒▒▒▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒█▒▒▄▀▒▒█████████
█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▒▒▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒█████████▒▒▄▀▒▒████▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
███████████████████████████████████████████████████████████████████████"""
)
site = input("\033[33mВведите адрес сайта http://")
os.system("wget -rkpE -nc -l 0 http://" + site)
print("Сайт находится в директории /MXtool/core/")
