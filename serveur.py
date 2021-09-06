import socket
from colorama import Back, Fore, Style, deinit, init
import json

with open('config.json') as f:
    config = json.load(f)


init()

HOST = config.get('host')
PORT = int(config.get('port'))

f.close()
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(1)

print(Fore.RED + Style.NORMAL + " /$$$$$$$  /$$   /$$       /$$$$$$$$ /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$")
print("| $$__  $$| $$  /$$/      |__  $$__//$$__  $$| $$  | $$ /$$__  $$|__  $$__/")
print("| $$  \ $$| $$ /$$/          | $$  | $$  \__/| $$  | $$| $$  \ $$   | $$   ")
print("| $$  | $$| $$$$$/           | $$  | $$      | $$$$$$$$| $$$$$$$$   | $$   ")
print("| $$  | $$| $$  $$           | $$  | $$      | $$__  $$| $$__  $$   | $$   ")
print("| $$  | $$| $$\  $$          | $$  | $$    $$| $$  | $$| $$  | $$   | $$   ")
print("| $$$$$$$/| $$ \  $$         | $$  |  $$$$$$/| $$  | $$| $$  | $$   | $$   ")
print("|_______/ |__/  \__/         |__/   \______/ |__/  |__/|__/  |__/   |__/   ")
print("                                                                           ")

print(Fore.BLUE + "[*]Serveur")

client, ip = socket.accept()
print ("Conected to ", HOST)

while True:
	requete_client = client.recv(500)
	requete_client = requete_client.decode('utf-8')
	print(Fore.WHITE + requete_client)
	if not requete_client :
		print("close")
		break
	msg = input("->")
	msg = msg.encode("utf-8")
	client.send(msg)
clint.close()
socket.close()

