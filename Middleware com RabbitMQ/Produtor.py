import pika
import psutil

# Conectar ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar o tópico (exchange) e definir o tipo como 'topic'
channel.exchange_declare(exchange='temperatures', exchange_type='topic')

# Obter a temperatura da CPU
temperature = psutil.sensors_temperatures()['cpu-thermal'][0].current

# Publicar a temperatura no tópico 'cpu.temperature'
channel.basic_publish(exchange='temperatures', routing_key='cpu.temperature', body=str(temperature))

# Fechar a conexão com o RabbitMQ
connection.close()
