import sys
from pickle import dumps, loads
from io import BytesIO, StringIO, TextIOWrapper

class ClinicIO:
    def __init__(self, clinic):
        self.clinic = clinic
        self.doctors_stream = self.doctors_to_bytes_stream()

    def doctors_to_bytes_stream(self):
        doctors_stream = BytesIO()
        doctors_len_bytes = str(len(self.clinic.doctors)).encode()
        message = doctors_len_bytes + b"\n"

        for doctor in self.clinic.doctors:
            full_name_bytes = doctor.full_name.encode()

            message += str(len(full_name_bytes)).encode() + b";"
            message += full_name_bytes + b";"
            message += doctor.license_code.encode() + b";"
            message += doctor.birthdate.encode() + b";"
            message += doctor.speciality.encode()  + b"\n"

        doctors_stream.write(message)

        return doctors_stream



    def stdout(self):
        self.doctors_stream.seek(0)

        encoded_msg = self.doctors_stream.getvalue()
        print(encoded_msg.decode(), end='')


    def capture_stdin(self):
        self._stdout = sys.stdout
        self._capture_stream = BytesIO()
        self._wrapped_stdout = TextIOWrapper(self._capture_stream)
        sys.stdout = self._wrapped_stdout

    def stop_capture(self):
        self._wrapped_stdout.flush()
        captured_output = self._capture_stream
        sys.stdout = self._stdout
        self.add_many_doctors(captured_output)



    def write_file(self, file_name = ''):
        self.doctors_stream.seek(0)
        if not file_name:
            file_name = self.clinic.name + "_doctors.bin"

        file = open(file_name, 'wb')
        encoded_msg = self.doctors_stream.getvalue()
        file.write(encoded_msg.decode())
        flie.close()

    def read_file(self, file_name = ''):
        if not file_name:
            file_name = self.clinic.name + "_doctors.bin"

        file = open(file_name, 'rb')
        self.add_many_doctors(file)



    def send_tcp(self, socket):
        self.doctors_stream.seek(0)

        encoded_msg = self.doctors_stream.getvalue()

        data = encoded_msg.read(1024)
        while data:
            socket.send(data)
            data = encoded_msg.read(1024)



    def add_many_doctors(self, bytes_stream):
        bytes_stream.seek(0)
        stream_msg = bytes_stream.getvalue().decode()
        stream = StringIO(stream_msg)

        total_doctors = int(stream.readline())

        line = stream.readline()
        while line:
            attributes = line[:-1].split(";")
            self.clinic.add_doctor(*attributes[1:])
            line = stream.readline()

        self.doctors_stream = self.doctors_to_bytes_stream()
