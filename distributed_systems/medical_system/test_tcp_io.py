from concurrent.futures import ThreadPoolExecutor
from functions import simple_server, simple_client
from functions import serialization_client, serialization_server_unchanged
from time import sleep

def test_copy_with_tcp(empty_clinic_io, filled_clinic_io, filled_clinic_output):
    with ThreadPoolExecutor() as executor:
        server_future = executor.submit(simple_server, empty_clinic_io)

        client_infos = [filled_clinic_io, filled_clinic_output]
        client_future = executor.submit(simple_client, *client_infos)

        server_future.result(timeout=1)
        copy_success = client_future.result(timeout=1)
        assert copy_success


