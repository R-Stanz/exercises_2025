from socket import socket, AF_INET, SOCK_STREAM
from Clinic import Clinic


clinic = Clinic("Luiza Redes Quixada", "Rodoviaria", "85 8998-23221")

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 11322))
s.listen()
conn, add = s.accept()

data = ""
try:
    while True:
        data += conn.recv(1024).decode()
        if not data:
            break
finally:
    conn.close() 

clinic.add_many_doctors(data)
