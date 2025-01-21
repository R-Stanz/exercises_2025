from Doctor import Doctor
from Ophthalmologist import Ophthalmologist
from Orthopedist import Orthopedist
from Psychiatrist import Psychiatrist

class Clinic:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.specialities = ["general", "ophthalmology", "orthopaedics", "psychiatry"]
        self.doctors = []

    def build_doctor(self, full_name, license_code, birthdate, speciality):
        doctor = ""
        if speciality == "general":
            doctor = Doctor(full_name, license_code, birthdate)
        elif speciality == "ophthalmology":
            doctor = Ophthalmologist(full_name, license_code, birthdate)
        elif speciality == "orthopaedics":
            doctor = Orthopedist(full_name, license_code, birthdate)
        elif speciality == "psychiatry":
            doctor = Psychiatrist(full_name, license_code, birthdate)

        return doctor

    def add_doctor(self, full_name, license_code, birthdate, speciality):
        doctor = self.build_doctor(full_name, license_code, birthdate, speciality)
        if not doctor or doctor in self.doctors:
            return
        
        self.doctors.append(doctor)
        return doctor

    def doctor_by_name(self, doctors_name):
        for doctor in self.doctors:
            if doctor.full_name == doctors_name:
                return doctor

    def doctor_by_license(self, license_code):
        for doctor in self.doctors:
            if doctor.license_code == license_code:
                return doctor

    def make_appointment(self, patient_name, date, doctors_name):
        doctor = self.make_appointment(doctors_name)
        doctor.appointments += 1


