import grpc
import meuservico_pb2
import meuservico_pb2_grpc

class MeuServicoImpl(meuservico_pb2_grpc.MeuServicoServicer):
    def MeuMetodo(self, request, context):
        resultado = "Olá, " + request.parametro1 + "! Você digitou o número " + str(request.parametro2)
        return meuservico_pb2.MeuResponse(resultado)

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meuservico_pb2_grpc.add_MeuServicoServicer_to_server(MeuServicoImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    start_server()


