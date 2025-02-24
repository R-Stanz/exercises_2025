from classes.Doctor import Doctor
from classes.specialities.Ophthalmology import Ophthalmologist
from classes.specialities.Orthopedics import Orthopedist
from classes.specialities.Psychiatry import Psychiatrist
from classes.specialities.Hematology import Hematologist
from io import BytesIO
from pickle import dumps

class Clinic:
    def __init__(self, name, address, phone):
        self.name = name.lower()
        self.address = address.lower()
        self.phone = phone
        self.specialities = ["general", "ophthalmology", "orthopaedics", "psychiatry", "hematology"]
        self.doctors = []



    def build_doctor(self, full_name, license_code, birthdate, speciality):
        doctor = ""
        speciality = speciality.lower()
        if speciality == "general":
            doctor = Doctor(full_name, license_code, birthdate)
        if speciality == "ophthalmology":
            doctor = Ophthalmologist(full_name, license_code, birthdate)
        if speciality == "orthopaedics":
            doctor = Orthopedist(full_name, license_code, birthdate)
        if speciality == "psychiatry":
            doctor = Psychiatrist(full_name, license_code, birthdate)
        if speciality == "hematology":
            doctor = Hematologist(full_name, license_code, birthdate)

        return doctor



    def add_doctor(self, full_name, license_code, birthdate, speciality):
        doctor = self.doctor_by_license(license_code)
        if doctor:
            return doctor
        
        doctor = self.build_doctor(full_name, license_code, birthdate, speciality)
        self.doctors.append(doctor)
        return doctor



    def doctor_by_name(self, doctors_name):
        for doctor in self.doctors:
            if doctor.full_name == doctors_name:
                return doctor



    def rm_doctor_by_license(self, license_code):
        filtered_doctors = []
        removed_doctor = {}
        for doc in self.doctors:
            if doc.license_code == license_code:
                removed_doctor = doc
            else:
                filtered_doctors.append(doc)

        self.doctors = filtered_doctors
        return removed_doctor



    def update_doctor_by_license(self, full_name, license_code, birthdate, speciality):
        for i, doc in enumerate(self.doctors):
            if doc.license_code == license_code:
                doctor = self.build_doctor(full_name, license_code, birthdate, speciality)
                self.doctors[i] = doctor
                return doctor
        return



    def doctor_by_license(self, license_code):
        for doctor in self.doctors:
            if doctor.license_code == license_code:
                return doctor



    def make_appointment(self, patient_name, date, doctors_name):
        doctor = self.make_appointment(doctors_name)
        doctor.appointments += 1



    def get_serialized_stream(self):
        stream = BytesIO()
        serialized_bytes = dumps(self)
        stream.write(serialized_bytes)

        return stream
