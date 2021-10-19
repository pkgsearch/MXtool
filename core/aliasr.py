import os
from textwrap import dedent

print(
    dedent(
        """\
            \033[36m
            ░█████╗░██╗░░░░░██╗░█████╗░░██████╗██████╗░
            ██╔══██╗██║░░░░░██║██╔══██╗██╔════╝██╔══██╗
            ███████║██║░░░░░██║███████║╚█████╗░██████╔╝
            ██╔══██║██║░░░░░██║██╔══██║░╚═══██╗██╔══██╗
            ██║░░██║███████╗██║██║░░██║██████╔╝██║░░██║
            ╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝"""
    )
)
choice = input(
    dedent(
        """\
            \033[35m[1]Android
            [2]Linux
            Выберите параметр (1 по умолчанию): """
    )
)

if choice == "2":
    bashrc = os.getenv("HOME") + "/.bashrc"
else:
    bashrc = os.getenv("PREFIX") + "/etc/bash.bashrc"

name = input("\033[33mВведите имя Алиаса: ")
use = input("Введите функцию алиаса в кавычках: ")
alias = "alias " + name + "=" + use
with open(bashrc, "w") as fp:
    fp.write(alias)
