from Clinic_doctors import Clinic_doctors
from Clinic import Clinic

clinic = Clinic("Health 2 Live", "8th St., MO", "232 432-5543")

clinic.add_doctor("Rafael Castro", "33432-KS", "02-25-1980", "orthopaedics")
clinic.add_doctor("Seth White", "5432-NC", "09-10-1995", "psychiatry")
clinic.add_doctor("Hannah Lontana", "12414325-NY", "07-04-2001", "general")

file = open("../clinic_doctors.bin", "wb")
clinic_doctors_infos_stream = Clinic_doctors(clinic, file)
clinic_doctors_infos_stream.send_infos()
file.close()
