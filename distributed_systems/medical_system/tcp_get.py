import sys
from socket import socket, AF_INET, SOCK_STREAM
from Clinic import Clinic


clinic = Clinic("Luiza Redes Quixada", "Rodoviaria", "85 8998-23221")

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(1)

conn, add = s.accept()

output = sys.stdout.buffer
data = conn.recv(1024)
while data:
    output.write(data)
    data = conn.recv(1024)

output.flush()
conn.close()
s.close()