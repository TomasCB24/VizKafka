from kafka import KafkaProducer
import json
import time
from sensors import generate_sensor_data

producer = KafkaProducer(bootstrap_servers=['localhost:29092', 'localhost:39092','localhost:49092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

sensor_types = ['Temperature', 'Motion', 'Light', 'Humidity', 'AirQuality', 'Sound', 'Water', 'DoorWindow']

while True:  # Bucle infinito para enviar datos continuamente
    for sensor_type in sensor_types:  # Iterar sobre cada tipo de sensor
        data = generate_sensor_data(sensor_type)
        topic_name = f'sensor-{sensor_type.lower()}'  # Generar nombre de tópico basado en tipo de sensor
        producer.send(topic_name, value=data)  # Usar el nombre del tópico para publicar
        print(f"Enviado a {topic_name}: {data}")  # Imprimir el dato enviado y el tópico
    producer.flush()  # Vaciar el productor después de enviar un conjunto de datos
    time.sleep(10)