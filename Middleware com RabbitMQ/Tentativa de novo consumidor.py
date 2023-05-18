import pika
import winsound

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar a fila
channel.exchange_declare(exchange='fire_detector', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='fire_detector', queue=queue_name)

# Definir a função de callback
def callback(ch, method, properties, body):
    print("Fire detected: %r" % body)
    winsound.Beep(1000, 2000)

# Consumir mensagens
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
