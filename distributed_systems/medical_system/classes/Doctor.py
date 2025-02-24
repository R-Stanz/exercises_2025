from classes.Appointment import Appointment
from Pyro5.api import expose

class Doctor(Appointment):
    def __init__(self, full_name, license_code, birthdate):
        self.first_name = full_name.split(" ")[0].lower()
        self.full_name = full_name.lower()
        self.license_code = license_code
        self.birthdate = birthdate
        self.speciality = "general"
        self.appointments_time = {}
        self.appointments = []


    @expose
    def make_an_appointment(self, patient, day, time):
        patient = patient.lower()
        if self.is_vacanct_time(day, time):
            if self.is_vacant_day(day):
                self.appointments_time[day] = {}
            self.appointments_time[day][time] = patient
            return True

        if self.time_has_same_patient(day, time, patient):
            return True

        return False


    @expose
    def time_has_same_patient(self, day, time, patient):
        appointments = self.appointments_time
        if day in appointments and \
            time in appointments[day] and \
            patient in appointments[day][time]:

                return True
        return False


    @expose
    def is_vacanct_time(self, day, time):
        if self.is_vacant_day(day):
            return True

        if time in self.appointments_time[day]:
            return False

        return True


    @expose
    def is_vacant_day(self, day):
        if day in self.appointments_time:
            return False
        return True


    def dict(self):
        return { 
            "full_name" : self.full_name,
            "license_code" : self.license_code,
            "birthdate" : self.birthdate,
            "speciality" : self.speciality
        }

    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False

        if self.full_name == other.full_name and self.license_code == other.license_code:
            return True
