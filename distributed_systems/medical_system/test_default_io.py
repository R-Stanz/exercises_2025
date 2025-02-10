def test_empty_clinic_stdout(empty_clinic_io, capsys):
    empty_clinic_io.stdout()
    captured = capsys.readouterr()
    assert captured.out == "0\n"


def test_filled_clinic_stdout(filled_clinic_io, filled_clinic_output, capsys):
    filled_clinic_io.stdout()
    captured = capsys.readouterr()
    assert captured.out == filled_clinic_output


def test_copy_with_stdin(std_cp_clinic_io, filled_clinic_output, capsys):
    std_cp_clinic_io.stdout()
    captured = capsys.readouterr()

    assert captured.out == filled_clinic_output
