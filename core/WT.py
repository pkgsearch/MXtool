import os
print("""\033[33m

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
███████████████████████████████████████████████████████████████████████""")
site = input("\033[33mВведите адрес сайта http://")
f = "wget -r -k -l 7 -p -E -nc "
h = "http://"
g = f+h+site
t = "termux-setup-storage && mv "+site+" ~/storage/shared/"
os.system(g)
n = input("Сайт находится в директории /xaker/core/"+site+" Если у вас termux введите y:")
if n == "y":
	os.system(t)
print("Сайт перемещён")

