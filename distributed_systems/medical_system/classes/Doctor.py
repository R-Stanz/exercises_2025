from classes.Appointment import Appointment

class Doctor(Appointment):
    def __init__(self, full_name, license_code, birthdate):
        self.first_name = full_name[0]
        self.full_name = full_name
        self.license_code = license_code
        self.birthdate = birthdate
        self.speciality = "general"
        self.appointments = 0

    def make_an_appointment(self):
        self.appointments += 1

    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False

        if self.full_name == other.full_name and self.license_code == other.license_code:
            return True
