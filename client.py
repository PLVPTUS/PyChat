import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
import sys

init(convert=True)

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

color = random.choice(colors)

IP = "127.0.0.1" # server address
PORT = 2024 # server port
sep = "<SEP>" 

sock = socket.socket()
print(f"{Fore.GREEN}[Connecting to {IP} ON PORT {PORT}...]")
sock.connect((IP, PORT))
print(f"{Fore.YELLOW}[Connected.]")
print(Fore.RESET)
name = input("Enter your name: ")
print(f"{Fore.RED}TYPE !q TO EXIT THE CHAT")

def listen_for_messages():
    while True:
        message = sock.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    message1 = input()
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    if message1.lower() == '!q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    message1 = f"{color}[{date_now}] {name}{sep}{message1}{Fore.RESET}"
    sock.send(message1.encode())

sock.close()