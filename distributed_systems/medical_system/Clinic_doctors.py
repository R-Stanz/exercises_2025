from Clinic import Clinic
from Doctor import Doctor

class Clinic_doctors:
    def __init__(self, clinic, destiny):
        self.clinic = clinic
        self.destiny = destiny

    def send_infos(self):
        doctors_len_bytes = str(len(self.clinic.doctors)).encode()
        self.destiny.write(doctors_len_bytes + b"\n")

        for doctor in self.clinic.doctors:
            full_name_bytes = doctor.full_name.encode()
            full_name_bytes_len = str(len(full_name_bytes)).encode()
            license_code_bytes = doctor.license_code.encode()
            birthdate_bytes = doctor.birthdate.encode()
            speciality_bytes = doctor.speciality.encode()

            self.destiny.write(full_name_bytes_len + b" ")
            self.destiny.write(full_name_bytes + b" ")
            self.destiny.write(license_code_bytes + b" ")
            self.destiny.write(birthdate_bytes + b" ")
            self.destiny.write(speciality_bytes + b"\n")

            '''
            self.destiny.write(b"Name Bytes Length: " + full_name_bytes_len + b"\n")
            self.destiny.write(b"Name: " + full_name_bytes + b"\n")
            self.destiny.write(b"License Code: " + license_code_bytes + b"\n")
            self.destiny.write(b"Birthdate: " + birthdate_bytes + b"\n")
            self.destiny.write(b"Speciality: " + speciality_bytes + b"\n\t-----\n")
            '''

        self.destiny.flush()
