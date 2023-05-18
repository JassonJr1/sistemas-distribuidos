# Cliente de Socket em Python

Este é um exemplo simples de um cliente de socket em Python que se conecta a um servidor em execução localmente.

## Funcionamento

1. Importe as bibliotecas necessárias:
   ```python
   import socket
   import threading
   from cryptography.fernet import Fernet
   
2. Defina as constantes:
HOST = 'localhost'  # O endereço do servidor (neste caso, é executado localmente)
PORT = 5058  # A porta utilizada para a comunicação com o servidor
SECRET_KEY = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='  # Chave secreta para criptografia

3. Crie um objeto Fernet com a chave secreta:
fernet = Fernet(SECRET_KEY)

4. Defina a função handle_response(conn) que será executada em uma thread separada para receber as respostas do servidor: 
def handle_response(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break

        mensagem_decodificada = fernet.decrypt(data).decode()
        print('Resposta do servidor:', mensagem_decodificada)

5. Defina a função start_client() para iniciar o cliente: 
def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    response_thread = threading.Thread(target=handle_response, args=(s,))
    response_thread.start()

    while True:
        mensagem = input('Digite uma mensagem para enviar ao servidor (ou "sair" para encerrar): ')

        if mensagem.lower() == 'sair':
            break

        mensagem_codificada = fernet.encrypt(mensagem.encode())
        s.sendall(mensagem_codificada)

    s.close()

6. Chame a função start_client() para iniciar o cliente:
start_client()

No start_client(), a função cria um objeto de socket, estabelece uma conexão com o servidor usando o endereço e a porta especificados e inicia uma thread separada para lidar com as respostas do servidor.

Em um loop contínuo, o cliente solicita ao usuário que digite uma mensagem para enviar ao servidor. Se o usuário digitar "sair", o loop será interrompido e a conexão será fechada.

Antes de enviar a mensagem ao servidor, ela é codificada usando a chave secreta fornecida e, em seguida, enviada através do socket para o servidor.

A função handle_response() é responsável por receber as respostas do servidor em um loop contínuo. Ela recebe os dados do socket, decodifica-os usando a chave secreta e imprime a resposta na tela. Quando não há mais dados recebidos, o loop é interrompido e a função termina.
