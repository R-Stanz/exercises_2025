from socket import socket, AF_INET, SOCK_STREAM
from Clinic_doctors import Clinic_doctors
from Clinic import Clinic
from os import remove, path

clinic = Clinic("Health 2 Live", "8th St., MO", "232 432-5543")

clinic.add_doctor("Rafael Castro", "33432-KS", "02-25-1980", "orthopaedics")
clinic.add_doctor("Seth White", "5432-NC", "09-10-1995", "psychiatry")
clinic.add_doctor("Hannah Lontana", "12414325-NY", "07-04-2001", "general")


tmp_file_path = 'tmp_clinic_doctors.bin'
if not path.exists(tmp_file_path):
    # Create the file if it does not exist
    file = open(tmp_file_path, 'wb')
    file.close()

file = open(tmp_file_path, 'r+b')
clinic_doctors_infos_stream = Clinic_doctors(clinic, file)
clinic_doctors_infos_stream.send_infos()

file.seek(0)

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 12345))
data = file.read(1024)
while data:
    s.send(data)
    data = file.read(1024)

s.close()
file.close()
remove(tmp_file_path)