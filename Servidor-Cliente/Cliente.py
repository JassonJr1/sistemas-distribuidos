import socket
import threading
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5058
SECRET_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

# Cria um objeto Fernet com a chave secreta
fernet = Fernet(SECRET_KEY)

def handle_response(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break

        mensagem_decodificada = fernet.decrypt(data).decode()
        print('Resposta do servidor:', mensagem_decodificada)

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Cria uma thread para receber as respostas do servidor
    response_thread = threading.Thread(target=handle_response, args=(s,))
    response_thread.start()

    while True:
        mensagem = input('Digite uma mensagem para enviar ao servidor (ou "sair" para encerrar): ')

        if mensagem.lower() == 'sair':
            break

        mensagem_codificada = fernet.encrypt(mensagem.encode())
        s.sendall(mensagem_codificada)

    s.close()

start_client()
