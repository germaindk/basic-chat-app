import socket
from colorama import Back, Fore, Style, deinit, init

init()

HOST = '192.168.1.42'
PORT = 6789

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print(Fore.RED + Style.NORMAL + " /$$$$$$$  /$$   /$$       /$$$$$$$$ /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$")
print("| $$__  $$| $$  /$$/      |__  $$__//$$__  $$| $$  | $$ /$$__  $$|__  $$__/")
print("| $$  \ $$| $$ /$$/          | $$  | $$  \__/| $$  | $$| $$  \ $$   | $$   ")
print("| $$  | $$| $$$$$/           | $$  | $$      | $$$$$$$$| $$$$$$$$   | $$   ")
print("| $$  | $$| $$  $$           | $$  | $$      | $$__  $$| $$__  $$   | $$   ")
print("| $$  | $$| $$\  $$          | $$  | $$    $$| $$  | $$| $$  | $$   | $$   ")
print("| $$$$$$$/| $$ \  $$         | $$  |  $$$$$$/| $$  | $$| $$  | $$   | $$   ")
print("|_______/ |__/  \__/         |__/   \______/ |__/  |__/|__/  |__/   |__/   ")
print("                                                                           ")

print(Fore.BLUE + "[*]Client")


socket.connect((HOST,PORT))

print ("Conected to ", HOST)



while True:
	msg = input("->")
	msg = msg.encode('utf-8')
	socket.send(msg)

	requete_serveur = socket.recv(500)
	requete_serveur =  requete_serveur.decode('utf-8')
	print(Fore.WHITE + requete_serveur)