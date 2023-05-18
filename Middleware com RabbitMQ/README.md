# Relatório - Middleware com RabbitMQ
## Requisitos

Certifique-se de ter instalado as seguintes bibliotecas antes de executar o código:

- `pika`
- `psutil`
- `winsound` (somente para sistemas Windows)

Você pode instalá-las usando o gerenciador de pacotes `pip`: pip install pika psutil

# Consumidor

Este é um exemplo de código em Python que ilustra como usar o RabbitMQ para enviar mensagens para uma fila. O código também utiliza a biblioteca `psutil` para obter a temperatura da CPU.

## Executando o código

1. Clone este repositório ou copie o código para um arquivo local.
2. Abra o arquivo Python em um ambiente de desenvolvimento ou editor de texto.
3. Execute o código Python.


## Funcionamento

O código está dividido em etapas para facilitar a compreensão. Aqui está uma explicação passo a passo do que o código faz:

1. Importar as bibliotecas `pika` e `psutil`.

```python
import pika
import psutil
```
Essas linhas importam as bibliotecas necessárias para se conectar ao RabbitMQ e obter informações sobre a CPU.

2. Conectar ao RabbitMQ.
```python
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
```
Essas linhas estabelecem uma conexão com um servidor RabbitMQ localmente na máquina ('localhost') e criam um canal de comunicação.

3. Criar Fila
```python
channel.queue_declare(queue='fire_detector')
```
Essa linha declara a criação de uma fila chamada 'fire_detector' no canal.

4. Obter a temperatura da CPU.
```python
cpu_temp = psutil.sensors_temperatures()['cpu-thermal'][0].current
```
Essa linha usa a função sensors_temperatures() do psutil para obter as informações de temperatura da CPU e armazena a temperatura atual na variável cpu_temp.

5. Verificar a temperatura da CPU e enviar uma mensagem para a fila se for alta o suficiente.
```python
if cpu_temp > 70:
    channel.basic_publish(exchange='', routing_key='fire_detector', body='Fire detected!')
```
Essas linhas verificam se a temperatura da CPU (cpu_temp) é maior que 70 graus Celsius. Se for, uma mensagem contendo o texto 'Fire detected!' é publicada na fila 'fire_detector' usando a função basic_publish().

6. Fechar a conexão com o RabbitMQ.
```python
connection.close()
```
# Tentativa de novo Consumidor

Este é um exemplo de código em Python que ilustra como consumir mensagens de uma fila no RabbitMQ. O código utiliza a biblioteca `pika` para se conectar ao RabbitMQ e a biblioteca `winsound` para reproduzir um som ao receber uma mensagem.


## Executando o Código

1. Clone este repositório ou copie o código para um arquivo local.

2. Abra o arquivo Python em um ambiente de desenvolvimento ou editor de texto.

3. Execute o código Python.

Certifique-se de executar o código em um sistema Windows para que o som seja reproduzido corretamente.

## Funcionamento

O código está dividido em etapas para facilitar a compreensão. Aqui está uma explicação passo a passo do que o código faz:

1. Importar as bibliotecas `pika` e `winsound`.

```python
import pika
import winsound
```
Essas linhas importam as bibliotecas necessárias para se conectar ao RabbitMQ e reproduzir um som.

2. Conectar ao RabbitMQ.
```python
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
```
Essas linhas estabelecem uma conexão com um servidor RabbitMQ localmente na máquina ('localhost') e criam um canal de comunicação.

3. Criar a fila.
```python
channel.exchange_declare(exchange='fire_detector', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='fire_detector', queue=queue_name)
```
Essas linhas declaram a criação de uma troca (exchange) chamada 'fire_detector' com o tipo 'fanout', que distribui as mensagens para todas as filas vinculadas a ela. Em seguida, declara uma fila anônima exclusiva e obtém o nome dessa fila. Por fim, vincula a fila à troca 'fire_detector'.

4. Definir a função de callback.
```python
def callback(ch, method, properties, body):
    print("Fire detected: %r" % body)
    winsound.Beep(1000, 2000)
```
Essa função é definida como um callback para ser executada quando uma mensagem for recebida. Ela imprime a mensagem recebida e reproduz um som usando a função Beep() do winsound.

5. Consumir mensagens.
```python
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
```
Essa linha configura o consumo de mensagens da fila queue_name usando a função basic_consume(). Quando uma mensagem é recebida, a função de callback callback() é executada.

6. Iniciar o consumo de mensagens.
```python
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```
Essas linhas imprimem uma mensagem indicando que o programa está esperando por mensagens e, em seguida, iniciam o consumo de mensagens da fila. O programa continuará consumindo mensagens indefinidamente até ser interrompido pelo pressionamento de CTRL+C.

Este exemplo pode ser útil para entender como consumir mensagens de uma fila no RabbitMQ usando Python e como adicionar um comportamento personalizado, como reproduzir um som, quando uma mensagem é recebida.

## Contribuição

Sinta-se à vontade para contribuir para este projeto. Você pode fazer isso abrindo um problema para relatar bugs ou sugerir melhorias, ou enviando um pull request com suas alterações propostas.
