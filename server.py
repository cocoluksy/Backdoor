# Imports
import socket

# Creating Listening Port

# host and port

# You can delete here after change HOST
if HOST == '127.0.0.1':
    print(f"[!] Don't forget to change default HOST:{HOST} to your HOST:{socket.gethostbyname(socket.gethostname())} in both server and client")

new_port = input('Input Host Port (Blank if default).')


server = socket.socket()
server.bind((HOST, PORT))

# Starting Server




# Reciving Commands
while True:
    