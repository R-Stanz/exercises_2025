from classes.Clinic import Clinic
from classes.Clinic_doctors import ClinicIO
import pytest

@pytest.fixture()
def empty_clinic_io():
    clinic = Clinic("Anything", "Somewhere", "999999")
    return ClinicIO(clinic)

def test_empty_clinic_stdout(empty_clinic_io, capsys):
    empty_clinic_io.stdout()
    captured = capsys.readouterr()
    assert captured.out == "0\n"



@pytest.fixture()
def filled_clinic_io():
    clinic = Clinic("Health 2 Live", "8th St., MO", "232 432-5543")

    clinic.add_doctor("Rafael Castro", "33432-KS", "02-25-1980", "orthopaedics")
    clinic.add_doctor("Seth White", "5432-NC", "09-10-1995", "psychiatry")
    clinic.add_doctor("Hannah Lontana", "12414325-NY", "07-04-2001", "general")

    return ClinicIO(clinic)

@pytest.fixture()
def filled_clinic_output():
    message = "3\n13;Rafael Castro;33432-KS;02-25-1980;orthopaedics\n"
    message += "10;Seth White;5432-NC;09-10-1995;psychiatry\n"
    message += "14;Hannah Lontana;12414325-NY;07-04-2001;general\n"
    return message

def test_filled_clinic_stdout(filled_clinic_io, filled_clinic_output, capsys):
    filled_clinic_io.stdout()
    captured = capsys.readouterr()
    assert captured.out == filled_clinic_output



@pytest.fixture()
def std_cp_clinic_io(filled_clinic_io, empty_clinic_io):
    empty_clinic_io.capture_stdin()
    filled_clinic_io.stdout()
    empty_clinic_io.stop_capture()

    return empty_clinic_io

def test_copy_with_stdin(std_cp_clinic_io, filled_clinic_output, capsys):
    std_cp_clinic_io.stdout()
    captured = capsys.readouterr()

    assert captured.out == filled_clinic_output
