import os
api_id = input("Введите API_ID: ")
api_hash = input("Введите API_HASH")
save = input("Сохранить ли пользователя в контактах если он существует: y/n")
if save == "y":
	s = 'True'
else:
	s = 'False'
c = """api_id = ' """ + api_id + """' 
api_hash = ' """ + api_hash + """ 'send_user = """ + s
f = open('config.py', 'w')
f.write(c)
f.close()
os.system("rm -f start.sh")
f = open('start.sh', 'w')
f.write("cd MXtool && cd core && cd tgc && python3 main.py")
f.close()
os.system("bash start.sh")
