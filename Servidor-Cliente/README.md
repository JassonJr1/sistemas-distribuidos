# Relatório - Servidor de Socket com Criptografia com Clientes

Este é um exemplo de um servidor de socket que recebe mensagens criptografadas de clientes, decifra essas mensagens, realiza alguma lógica com elas (se necessário), converte as mensagens em letras maiúsculas, criptografa a resposta e envia de volta ao cliente.

## Requisitos

- Python 3.x
- Bibliotecas: `socket`, `threading`, `cryptography`

# Servidor
## Configuração

Antes de executar o servidor, é necessário configurar as seguintes constantes:

- `HOST`: O endereço IP do servidor. Por exemplo, `'localhost'` indica que o servidor está sendo executado na mesma máquina.
- `PORT`: O número da porta em que o servidor estará ouvindo as conexões.
- `SECRET_KEY`: A chave secreta usada pelo algoritmo de criptografia para codificar e decodificar as mensagens.

Certifique-se de ter instalado as bibliotecas necessárias, que podem ser instaladas com o seguinte comando: pip install cryptography


## Executando o Servidor

Execute o arquivo Python `server.py` para iniciar o servidor. O servidor começará a ouvir as conexões de entrada na porta especificada.


## Funcionamento

1. O servidor cria um objeto `Fernet` com a chave secreta fornecida.
2. O servidor aguarda conexões de clientes.
3. Para cada nova conexão, é criada uma nova thread para lidar com o cliente.
4. A função `handle_client` é executada na thread do cliente para receber e processar as mensagens.
5. A mensagem recebida é decodificada usando a chave secreta e exibida no console.
6. Se necessário, alguma lógica adicional pode ser aplicada à mensagem recebida.
7. A mensagem é convertida em letras maiúsculas.
8. A mensagem de resposta é criptografada usando a mesma chave secreta.
9. A mensagem criptografada é enviada de volta ao cliente.
10. O processo continua até que não haja mais dados recebidos do cliente, momento em que a conexão é encerrada.

# Cliente 
## Configuração

Antes de executar o cliente, é necessário configurar as seguintes constantes:

- `HOST`: O endereço IP do servidor. Por exemplo, `'localhost'` indica que o servidor está sendo executado na mesma máquina.
- `PORT`: O número da porta em que o servidor está ouvindo as conexões.
- `SECRET_KEY`: A chave secreta usada pelo algoritmo de criptografia para codificar e decodificar as mensagens. Certifique-se de usar a mesma chave usada pelo servidor.

Certifique-se de ter instalado as bibliotecas necessárias, que podem ser instaladas com o seguinte comando: pip install cryptography


## Executando o Cliente

Execute o arquivo Python `client.py` para iniciar o cliente. O cliente se conectará ao servidor especificado.


## Funcionamento

1. O cliente cria um objeto `Fernet` com a chave secreta fornecida.
2. O cliente se conecta ao servidor através do endereço e porta fornecidos.
3. É criada uma thread separada para lidar com as respostas recebidas do servidor.
4. O cliente entra em um loop infinito para solicitar ao usuário que digite uma mensagem para enviar ao servidor.
5. Se a mensagem digitada for "sair", o loop é interrompido e o cliente é encerrado.
6. A mensagem é criptografada usando a mesma chave secreta.
7. A mensagem criptografada é enviada ao servidor.
8. O cliente continua no loop, permitindo que o usuário envie mais mensagens ao servidor.
9. A thread de respostas do servidor continua em execução, recebendo e decodificando as respostas recebidas do servidor e exibindo-as no console.

## Contribuição

Sinta-se à vontade para contribuir para este projeto. Você pode fazer isso abrindo um problema para relatar bugs ou sugerir melhorias, ou enviando um pull request com suas alterações propostas.

