import struct
import socket
import sys

class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class PessoasOutputStream:
    def __init__(self, pessoas, destino):
        self.pessoas = pessoas
        self.destino = destino

    def enviar_dados(self):
        numero_de_pessoas = len(self.pessoas)
        self.destino.write(struct.pack('>I', numero_de_pessoas))

        for pessoa in self.pessoas:
            nome_bytes = pessoa.nome.encode()
            len_bytes = str(len(nome_bytes)).encode()
            cpf_bytes = pessoa.cpf.encode()
            idade_bytes = str(pessoa.idade).encode()

            self.destino.write(len_bytes + b" ")
            self.destino.write(nome_bytes + b" ")
            self.destino.write(cpf_bytes + b" ")
            self.destino.write(idade_bytes)
            self.destino.write(b"\n")

        self.destino.flush()

# Teste com saída padrão
def teste_saida_padrao():
    pessoas = [
        Pessoa("Alice", "12345678900", 30),
        Pessoa("Bob", "09876543211", 25)
    ]
    stream = PessoasOutputStream(pessoas, sys.stdout.buffer)
    stream.enviar_dados()

# Teste com arquivo
def teste_arquivo():
    pessoas = [
        Pessoa("Alice", "12345678900", 30),
        Pessoa("Bob", "09876543211", 25)
    ]
    with open("pessoas.bin", "wb") as f:
        stream = PessoasOutputStream(pessoas, f)
        stream.enviar_dados()

# Teste com servidor remoto (TCP)
def teste_servidor_remoto():
    pessoas = [
        Pessoa("Alice", "12345678900", 30),
        Pessoa("Bob", "09876543211", 25)
    ]
    servidor = ("localhost", 12345)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(servidor)
        stream = PessoasOutputStream(pessoas, s.makefile('wb'))
        stream.enviar_dados()

if __name__ == "__main__":
    # Escolha o teste a ser executado
    #teste_saida_padrao()
    # teste_arquivo()
    #teste_servidor_remoto()

