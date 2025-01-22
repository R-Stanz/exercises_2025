from Clinic import Clinic

clinic = Clinic("Luiza Redes Quixada", "Rodoviaria", "85 8998-23221")
data = open('./clinic_doctors.bin', 'rb')
data = data.read()
data = data.decode()
clinic.add_many_doctors(data)
#print(len(clinic.doctors))
