from functions import rmi_server
from functions import rmi_client_appointment_empty_schedule
from functions import rmi_client_appointment_repeated
from functions import rmi_client_appointment_clash
from functions import rmi_client_appointment_2_in_a_day

from concurrent.futures import ThreadPoolExecutor
from time import sleep
from subprocess import Popen


def make_an_appointment(rmi_client, selected_doctor):
    pyro_ns_process = Popen("pyro5-ns", shell=True)
    sleep(0.01)

    with ThreadPoolExecutor() as executor:
        print("Init Server Thread")
        server_future = executor.submit(rmi_server, *[selected_doctor, pyro_ns_process])

        print("Init Client Thread")
        client_future = executor.submit(rmi_client)

        server_future.result()
        has_booked = client_future.result()
        return has_booked


def test_rmi_appointment_empty_schedule(filled_clinic_io):
    selected_doctor = filled_clinic_io.clinic.doctors[0]
    assert make_an_appointment(rmi_client_appointment_empty_schedule, selected_doctor)

def test_rmi_appointment_repeated(filled_clinic_io):
    selected_doctor = filled_clinic_io.clinic.doctors[0]
    assert make_an_appointment(rmi_client_appointment_repeated, selected_doctor)

def test_rmi_client_appointment_clash(filled_clinic_io):
    selected_doctor = filled_clinic_io.clinic.doctors[0]
    assert not make_an_appointment(rmi_client_appointment_clash, selected_doctor)

def test_rmi_client_appointment_2_in_a_day(filled_clinic_io):
    selected_doctor = filled_clinic_io.clinic.doctors[0]
    assert make_an_appointment(rmi_client_appointment_2_in_a_day, selected_doctor)
