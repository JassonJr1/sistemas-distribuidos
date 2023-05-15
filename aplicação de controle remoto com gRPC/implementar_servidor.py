import controle_remoto_pb2
import controle_remoto_pb2_grpc

class DispositivoRemotoServicer(controle_remoto_pb2_grpc.DispositivoRemotoServicer):
  def Ligar(self, request, context):
    # Lógica para ligar o dispositivo
    return controle_remoto_pb2.Resultado(sucesso=True)

  def Desligar(self, request, context):
    # Lógica para desligar o dispositivo
    return controle_remoto_pb2.Resultado(sucesso=True)

# Inicia o servidor gRPC e adiciona o serviço ao servidor
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  controle_remoto_pb2_grpc.add_DispositivoRemotoServicer_to_server(DispositivoRemotoServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

# Inicia o servidor quando o arquivo é executado diretamente
if __name__ == '__main__':
  serve()
