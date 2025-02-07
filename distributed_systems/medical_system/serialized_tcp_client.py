from socket import socket, AF_INET, SOCK_STREAM
from Clinic_doctors import Clinic_doctors
from Clinic import Clinic
from pickle import loads, dumps
from io import BytesIO


def new_clinic():
    clinic = Clinic("Health 2 Live", "8th St., MO", "232 432-5543")

    clinic.add_doctor("Rafael Castro", "33432-KS", "02-25-1980", "orthopaedics")
    clinic.add_doctor("Seth White", "5432-NC", "09-10-1995", "psychiatry")
    clinic.add_doctor("Hannah Lontana", "12414325-NY", "07-04-2001", "general")

    return clinic

def send_serialized_clinic(clinic):
    message = BytesIO()

    serialized_bytes = dumps(clinic)
    message.write(serialized_bytes)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1', 12345))

    message.seek(0)
    data = message.read(1024)
    while data:
        s.send(data)
        data = message.read(1024)

    s.close()
    message.close()

def get_serialized_clinic():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('127.0.0.1', 12346))
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

clinic = new_clinic()
print("Sending serialized clinic: " + clinic.name + ".")
send_serialized_clinic(clinic)

print("Getting a serialized clinic.")
clinic = get_serialized_clinic()
print("Got the clinic: " + clinic.name + "!")
