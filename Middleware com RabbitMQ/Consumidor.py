import pika
import psutil

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar a fila
channel.queue_declare(queue='fire_detector')

# Obter a temperatura da CPU
cpu_temp = psutil.sensors_temperatures()['cpu-thermal'][0].current

# Verificar a temperatura da CPU e enviar uma mensagem para a fila se for alta o suficiente
if cpu_temp > 70:
    channel.basic_publish(exchange='', routing_key='fire_detector', body='Fire detected!')

# Fechar a conexão com o RabbitMQ
connection.close()
