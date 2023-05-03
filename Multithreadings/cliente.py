import socket
import threading
import time

HOST = 'localhost'
PORT = 5000

def send_request(s, request):
    s.sendall(request.encode())
    response = s.recv(1024)
    #print('Resposta:', response.decode())
    s.close()

def start_client(num_requests, message_size):
    requests = ['a' * message_size]

    for i in range(num_requests):
        threads = []
        for request in requests:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            t = threading.Thread(target=send_request, args=(s, request))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

    #time.sleep(1)

if __name__ == '__main__':
    start_client(num_requests=100, message_size=512)
