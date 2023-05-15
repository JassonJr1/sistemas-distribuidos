import controle_remoto_pb2
import controle_remoto_pb2_grpc
import grpc

class ClienteDispositivoRemoto:
  def __init__(self):
    # Cria um canal para se conectar ao servidor
    self.canal = grpc.insecure_channel('localhost:50051')
    # Cria um stub para chamar os métodos do serviço
    self.stub = controle_remoto_pb2_grpc.DispositivoRemotoStub(self.canal)

  def ligar_dispositivo(self, nome):
    # Cria uma mensagem Dispositivo com o nome do dispositivo
    dispositivo = controle_remoto_pb2.Dispositivo(nome=nome)
    # Chama o método Ligar do serviço, passando a mensagem Dispositivo como parâmetro
    resultado = self.stub.Ligar(dispositivo)
    return resultado.sucesso

  def desligar_dispositivo(self, nome):
    # Cria uma mensagem Dispositivo com
