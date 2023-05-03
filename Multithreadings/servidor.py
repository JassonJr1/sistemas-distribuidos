import socket
import threading

HOST = 'localhost'
PORT = 5000

def handle_client(conn, addr):
    print('Conectado por', addr)
    data = conn.recv(1024)
    if not data:
        return
    if data.decode() == 'echo':
        conn.sendall(data)
    elif data.decode() == 'reply':
        conn.sendall(b'Resposta pre-definida')
    elif data.decode() == 'reverse':
        conn.sendall(data[::-1])
    else:
        conn.sendall(b'Servico nao disponivel')
    conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print('Servidor iniciado em', HOST, PORT)

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()

if __name__ == '__main__':
    start_server()
