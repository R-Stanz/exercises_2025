from io import BytesIO
from hashlib import md5

def get_file_as_stream(file_name):
    stream = BytesIO()
    file = open(file_name, 'rb')

    data = file.read(1024)
    while data:
        stream.write(data)
        data = file.read(1024)

    file.close()
    stream.seek(0)

    return stream


def get_file_md5(file_name):
    md5_obj = md5()
    file = open(file_name, 'rb')

    data = file.read(1024)
    while data:
        md5_obj.update(data)
        data = file.read(1024)

    file.close()
    return md5_obj.hexdigest()


def test_empty_clinic_file_output(empty_clinic_io):
    empty_clinic_io.write()

    file_name = empty_clinic_io.clinic.name + "_doctors.bin"
    stream = get_file_as_stream(file_name)

    assert stream.getvalue() == b"0\n"


def test_filled_clinic_file_output(filled_clinic_io, filled_clinic_output):
    filled_clinic_io.write()

    file_name = filled_clinic_io.clinic.name + "_doctors.bin"
    stream = get_file_as_stream(file_name)

    assert stream.getvalue() == filled_clinic_output.encode()


def test_copy_with_files_io(filled_clinic_io, empty_clinic_io, filled_clinic_output, capsys):
    filled_clinic_io.write()
    filled_file_name = filled_clinic_io.clinic.name + "_doctors.bin"
    filled_md5 = get_file_md5(filled_file_name)

    empty_clinic_io.read(filled_file_name)
    copy_file_name = empty_clinic_io.clinic.name + "_doctors.bin"
    copy_md5 = get_file_md5(copy_file_name)

    assert filled_md5 == copy_md5
