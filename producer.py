from kafka import KafkaProducer
import json
import random
from sensors import generate_sensor_data

producer = KafkaProducer(bootstrap_servers=['localhost:29092', 'localhost:39092','localhost:49092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

sensor_types = ['Temperature', 'Motion', 'Light', 'Humidity', 'AirQuality', 'Sound', 'Water', 'DoorWindow']

# Generar y enviar datos de sensor
for _ in range(20):
    sensor_type = random.choice(sensor_types)
    data = generate_sensor_data(sensor_type)
    producer.send('sensor-data', value=data)

producer.flush()
