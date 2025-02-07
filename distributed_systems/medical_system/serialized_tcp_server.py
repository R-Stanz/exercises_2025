from socket import socket, AF_INET, SOCK_STREAM
from Clinic import Clinic
from io import BytesIO
from pickle import loads, dumps

def get_serialized_clinic():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('127.0.0.1', 12345))
    s.listen(1)

    conn, add = s.accept()

    message = BytesIO()
    data = conn.recv(1024)
    while data:
        message.write(data)
        data = conn.recv(1024)

    conn.close()
    s.close()

    message.seek(0)
    return loads(message.getvalue())

def send_serialized_clinic(clinic):
    message = BytesIO()

    serialized_bytes = dumps(clinic)
    message.write(serialized_bytes)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1', 12346))

    message.seek(0)
    data = message.read(1024)
    while data:
        s.send(data)
        data = message.read(1024)

    s.close()
    message.close()


print("Getting serialized clinic...")

clinic = get_serialized_clinic()
print("Got the clinic: " + clinic.name + ".")

clinic.name = "Columbus"
print("Renamed clinic to: " + clinic.name + ".")
print("Sending modified clinic.")
send_serialized_clinic(clinic)
print("Sent!")
