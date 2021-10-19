import os

os.system("clear")

if not os.path.exists("config.py"):
    api_id = input("Введите API_ID: ")
    api_hash = input("Введите API_HASH")
    save = input("Сохранить ли пользователя в контактах если он существует: y/n")
    if save == "y":
        s = "True"
    else:
        s = "False"
    c = (
        """api_id = ' """
        + api_id
        + """ + ' 
    api_hash = ' """
        + api_hash
        + """' 
    send_user = """
        + s
    )

    with open("config.py", "w") as config:
        f.write(c)

import tgc_main
