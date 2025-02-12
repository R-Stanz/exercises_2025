from concurrent.futures import ThreadPoolExecutor
from functions import rmi_server, rmi_client_appointment_on_empty_schedule
from time import sleep
from subprocess import Popen

def test_rmi_appointment_on_empty_schedule(filled_clinic_io):
    pyro_ns_process = Popen("pyro5-ns", shell=True)
    sleep(0.01)

    with ThreadPoolExecutor() as executor:
        selected_doctor = filled_clinic_io.clinic.doctors[0]
        print("Init Server Thread")
        server_future = executor.submit(rmi_server, *[selected_doctor, pyro_ns_process])

        print("Init Client Thread")
        rmi_client = rmi_client_appointment_on_empty_schedule
        client_future = executor.submit(rmi_client)


        server_future.result()
        has_booked = client_future.result()
        assert has_booked
