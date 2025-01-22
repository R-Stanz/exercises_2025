from Clinic import Clinic
from Doctor import Doctor

class Clinic_doctors:
    def __init__(self, clinic, remote):
        self.clinic = clinic
        self.remote = remote

    def send_infos(self):
        doctors_len_bytes = str(len(self.clinic.doctors)).encode()
        self.remote.write(doctors_len_bytes + b"\n")

        for doctor in self.clinic.doctors:
            full_name_bytes = doctor.full_name.encode()
            full_name_bytes_len = str(len(full_name_bytes)).encode()
            license_code_bytes = doctor.license_code.encode()
            birthdate_bytes = doctor.birthdate.encode()
            speciality_bytes = doctor.speciality.encode()

            self.remote.write(full_name_bytes_len + b";")
            self.remote.write(full_name_bytes + b";")
            self.remote.write(license_code_bytes + b";")
            self.remote.write(birthdate_bytes + b";")
            self.remote.write(speciality_bytes + b"\n")

            '''
            self.remote.write(b"Name Bytes Length: " + full_name_bytes_len + b"\n")
            self.remote.write(b"Name: " + full_name_bytes + b"\n")
            self.remote.write(b"License Code: " + license_code_bytes + b"\n")
            self.remote.write(b"Birthdate: " + birthdate_bytes + b"\n")
            self.remote.write(b"Speciality: " + speciality_bytes + b"\n\t-----\n")
            '''

        self.remote.flush()

