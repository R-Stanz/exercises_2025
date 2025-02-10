from socket import socket, AF_INET, SOCK_STREAM, SHUT_WR
from io import BytesIO
from hashlib import md5
from io import BytesIO

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


def stream_md5(stream):
    hashing = md5()

    data = stream.read(1024)
    while data:
        hashing.update(data)
        data = stream.read(1024)

    return hashing.hexdigest()


def get_file_md5(file_name):
    file_stream = get_file_as_stream(file_name)
    return stream_md5(file_stream)


def receive_tcp_input_stream(socket):
    stream = BytesIO()
    data = socket.recv(1024)
    while data:
        stream.write(data)
        data = socket.recv(1024)

    stream.seek(0)
    return stream


def simple_server(clinic_io):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('127.0.0.1', 12345))
    s.listen(1)

    conn, add = s.accept()

    clinic_io.get_tcp(conn)
    clinic_io.send_tcp(conn)

    conn.shutdown(SHUT_WR)
    conn.close()
    s.close()


def simple_client(clinic_io, expected_confirmation):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('127.0.0.1', 12345))
    clinic_io.send_tcp(s)
    s.shutdown(SHUT_WR)

    input_stream = receive_tcp_input_stream(s)
    s.close()

    input_md5 = stream_md5(input_stream)
    input_stream.close()

    expected_confirmation_stream = BytesIO(expected_confirmation.encode())
    expected_md5 = stream_md5(expected_confirmation_stream)
    expected_confirmation_stream.close()

    return input_md5 == expected_md5

