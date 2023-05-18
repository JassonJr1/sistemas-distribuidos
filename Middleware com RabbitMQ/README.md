# Relatório - Middleware com RabbitMQ
## Requisitos

Certifique-se de ter instalado as seguintes bibliotecas antes de executar o código:

- pika
- psutil

Você pode instalá-las usando o gerenciador de pacotes `pip`: pip install pika psutil

## Detector de Incendio

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
