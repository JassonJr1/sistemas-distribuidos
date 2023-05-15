syntax = "proto3";

package controle_remoto;

// Define o serviço que será oferecido pelo servidor
service DispositivoRemoto {
  // Método para ligar o dispositivo
  rpc Ligar(Dispositivo) returns (Resultado) {}
  // Método para desligar o dispositivo
  rpc Desligar(Dispositivo) returns (Resultado) {}
}

// Mensagem para representar o dispositivo
message Dispositivo {
  string nome = 1;
}

// Mensagem para representar o resultado da operação
message Resultado {
  bool sucesso = 1;
}
