class Doctor:
    def __init__(self, full_name, license_code, birthdate):
        self.first_name = full_name[0]
        self.full_name = full_name
        self.license_code = license_code
        self.birthdate = birthdate
        self.speciality = "general"
        self.appointments = 0

    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False

        if self.full_name == other.full_name and self.license_code == other.license_code:
            return True
