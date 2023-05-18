import grpc
import meuservico_pb2
import meuservico_pb2_grpc


def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = meuservico_pb2_grpc.MeuServicoStub(channel)

    # Criação da mensagem de request
    request = meuservico_pb2.MeuRequest(parametro1='Alice', parametro2=42)

    # Chamada do método remoto
    response = stub.MeuMetodo(request)
    print("Resposta do servidor:", response.resultado)

if __name__ == '__main__':
    run_client()
