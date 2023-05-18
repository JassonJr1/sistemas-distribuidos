<!DOCTYPE html>
<html>
<head>
  <title>Detector de Incêndio</title>
</head>
<body>
  <h1>Detector de Incêndio</h1>
  <p>Este é um exemplo de código para simular a detecção de incêndio em um ambiente utilizando a temperatura da CPU como referência.</p>

  <h2>Código do Produtor</h2>
  <pre>
    <code>
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
    </code>
  </pre>

  <p>O código do produtor estabelece uma conexão com o RabbitMQ, cria uma fila chamada "fire_detector" e obtém a temperatura da CPU. Se a temperatura for superior a 70 graus Celsius, uma mensagem indicando a detecção de incêndio é enviada para a fila.</p>

  <h2>Código do Consumidor</h2>
  <pre>
    <code>
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
    </code>
  </pre>

  <p>O código do consumidor estabelece uma conexão com o RabbitMQ, cria uma fila e define uma função de callback que será chamada sempre que uma mensagem for recebida na fila. Neste exemplo, a função de callback imprime a mensagem recebida e aciona um alarme sonoro.</p>

  <p>Lembre-se de executar esses códigos em um ambiente Python adequado, com as bibliotecas `pika` e `psutil` instaladas. Além disso, certifique-se de ter o RabbitMQ em execução e configurado corretamente.</p>
</body>
</html>