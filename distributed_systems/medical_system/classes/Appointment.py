from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def make_an_appointment(self):
        pass
