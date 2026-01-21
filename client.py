import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8000))

message = client.recv(1024).decode()
username = input(message.encode())
message = client.recv(1024).decode()
username = input(message.encode())
client.send(username.encode())
