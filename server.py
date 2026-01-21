import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))

server.listen()

def handle_connection(c):
    c.send ("username: ".encode())
    username = c.recv(1024).decode()
    c.send ("password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

    if cur.fetchall():
        c.send("You are logged in".encode())
    else:
        c.send("Login failed, please try again later".encode())

        while True:
            c, addr = server.accept()
            threading.Thread(target=handle_connection, args=(c,)).start()