import socket
from threading import Thread
from colorama import Fore, init, Back

init(convert=True)

IP = "0.0.0.0" # server ip
PORT = 2024 # server port 
sep = "<SEP>" 

client_sockets = set()
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP, PORT))

sock.listen(5)
print(f"{Fore.GREEN}[WAITING FOR CONNECTIONS ON {IP} AT PORT {PORT}]")

def listen(cs):
    while True:
        try:
            message = cs.recv(1024).decode()
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            message = message.replace(sep, ": ")
        for client_socket in client_sockets:
            client_socket.send(message.encode())

while True:
    client_socket, client_address = sock.accept()
    print(f"{Fore.YELLOW} [{client_address} connected.]")
    client_sockets.add(client_socket)
    t = Thread(target=listen, args=(client_socket,))
    t.daemon = True
    t.start()

for cs in client_sockets:
    cs.close()
sock.close()