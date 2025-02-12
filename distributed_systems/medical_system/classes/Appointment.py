from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def make_an_appointment(self, patient, day, time):
        pass

    @abstractmethod
    def time_has_same_patient(self, day, time, patient):
        pass

    @abstractmethod
    def is_vacanct_time(self, day, time):
        pass

    @abstractmethod
    def is_vacant_day(self, day):
        pass
