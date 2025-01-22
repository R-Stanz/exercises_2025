import subprocess
from Clinic import Clinic

result = subprocess.run(['python3', './default_send.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')
clinic = Clinic("Luiza Redes Quixada", "Rodoviaria", "85 93843-3422")
clinic.add_many_doctors(result)
