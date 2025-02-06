from socket import socket, AF_INET, SOCK_STREAM
from Clinic_doctors import Clinic_doctors
from Clinic import Clinic
from io import BytesIO

clinic = Clinic("Health 2 Live", "8th St., MO", "232 432-5543")

clinic.add_doctor("Rafael Castro", "33432-KS", "02-25-1980", "orthopaedics")
clinic.add_doctor("Seth White", "5432-NC", "09-10-1995", "psychiatry")
clinic.add_doctor("Hannah Lontana", "12414325-NY", "07-04-2001", "general")

message = BytesIO()
clinic_doctors_infos_stream = Clinic_doctors(clinic, message)
clinic_doctors_infos_stream.send_infos()


s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 12345))

message.seek(0)
data = message.read(1024)

while data:
    s.send(data)
    data = message.read(1024)

s.close()
message.close()
