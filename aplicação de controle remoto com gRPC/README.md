# Relatório - Chamada de Procedimento Remoto com gRPC em Python

Este relatório descreve o processo de implementação e execução de uma chamada de procedimento remoto (RPC) utilizando gRPC em Python.

## Funcionamento

A seguir estão as etapas necessárias para implementar e executar uma chamada de procedimento remoto com gRPC em Python:

1. **Definir o arquivo `.proto`**: Crie um arquivo `.proto` para definir a estrutura e as operações do serviço gRPC. Certifique-se de especificar as mensagens e as chamadas de procedimento remoto necessárias.

2. **Compilar o arquivo `.proto`**: Utilize o compilador do gRPC para gerar os arquivos Python correspondentes ao serviço. No terminal, execute o seguinte comando:
Python correspondentes ao serviço. No terminal, execute o seguinte comando:
``````CSS
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. meuservico.proto
``````

Isso irá gerar os arquivos `meuservico_pb2.py` e `meuservico_pb2_grpc.py` que contêm as classes e métodos necessários para usar gRPC em Python.

3. **Implementar o servidor gRPC**: Crie um arquivo Python para implementar o servidor gRPC. Importe os arquivos gerados (`meuservico_pb2.py` e `meuservico_pb2_grpc.py`) e implemente a lógica do servidor, definindo uma classe que herde da classe `MeuServicoServicer` e sobrescreva os métodos definidos no arquivo `.proto`.

4. **Iniciar o servidor gRPC**: No arquivo do servidor, crie uma função para iniciar o servidor gRPC. Crie uma instância do servidor, adicione o serviço implementado e defina a porta em que o servidor irá ouvir. Em seguida, inicie o servidor chamando o método `start()`.

5. **Implementar o cliente gRPC**: Crie um arquivo Python separado para o cliente. Importe os mesmos arquivos gerados (`meuservico_pb2.py` e `meuservico_pb2_grpc.py`). Crie uma função para executar o cliente gRPC. Crie um canal de comunicação com o servidor gRPC, crie uma instância do stub (cliente) do serviço e faça chamadas aos métodos remotos definidos no arquivo `.proto`.

6. **Executar o servidor e o cliente**: Abra dois terminais separados. No primeiro terminal, execute o arquivo do servidor com o comando `python nome_do_arquivo.py`. Isso iniciará o servidor gRPC e ele começará a ouvir as solicitações na porta especificada. No segundo terminal, execute o arquivo do cliente com o comando `python nome_do_arquivo.py`. Isso executará a chamada de procedimento remoto e você verá a resposta do servidor impressa no terminal.

Lembre-se de substituir `meuserv

## Contribuição

Sinta-se à vontade para contribuir para este projeto. Você pode fazer isso abrindo um problema para relatar bugs ou sugerir melhorias, ou enviando um pull request com suas alterações propostas.
