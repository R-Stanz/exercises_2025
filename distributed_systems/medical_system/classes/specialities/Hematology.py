from classes.Doctor import Doctor

class Hematologist(Doctor):
    def __init__(self, full_name, license_code, birthdate):
        super().__init__(full_name, license_code, birthdate)
        self.speciality = "hematology" 
