from Doctor import Doctor

class Psychiatrist(Doctor):
    def __init__(self, full_name, license_code, birthdate):
        super().__init__(full_name, license_code, birthdate)
        self.speciality = "psychiatry" 
