from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('sensor-data',
                         bootstrap_servers=['localhost:29092', 'localhost:39092','localhost:49092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Procesar mensajes
for message in consumer:
    data = message.value
    print(f"Recibido: {data}")
