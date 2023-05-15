import controle_remoto_pb2
import controle_remoto_pb2_grpc

# Compila o arquivo .proto e gera o código Python correspondente
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. controle_remoto.proto
