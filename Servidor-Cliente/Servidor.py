import socket
import threading
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5058
SECRET_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

# Cria um objeto Fernet com a chave secreta
fernet = Fernet(SECRET_KEY)

def handle_client(conn, addr):
    print('Cliente conectado:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break

        mensagem_codificada = data
        mensagem_decodificada = fernet.decrypt(mensagem_codificada).decode()
        print('Mensagem recebida do cliente:', mensagem_decodificada)

        # Realiza alguma lógica com a mensagem recebida, se necessário

        # Transforma a mensagem em letra maiúscula
        mensagem_decodificada = mensagem_decodificada.upper()

        # Criptografa a mensagem de resposta
        mensagem_codificada = fernet.encrypt(mensagem_decodificada.encode())

        # Envia a resposta de volta ao cliente
        conn.sendall(mensagem_codificada)

    conn.close()
    print('Cliente desconectado:', addr)

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print('Aguardando conexões de clientes...')

    while True:
        conn, addr = s.accept()
        print('Cliente conectado:', addr)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()
