from kafka import KafkaConsumer
import json
import psycopg2

print("Iniciando consumidor...")

conn = psycopg2.connect(
        dbname="postgres",
        user="timescaledb",
        password="password",
        host="localhost",
        port="5432"
    )

print("Conectado a la base de datos")
cursor = conn.cursor()

print("Esperando mensajes...")

consumer = KafkaConsumer('sensor-data',
                         bootstrap_servers=['localhost:29092', 'localhost:39092','localhost:49092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Procesar mensajes
for message in consumer:
    data = message.value
    print(f"Recibido: {data}")
    sensor_type = data['type']
    value = data['value']
    timestamp = data['timestamp']

    print(f"Insertando datos en la base de datos: {sensor_type}, {value}, {timestamp}")

    try:
        cursor.execute(
            "INSERT INTO sensor (type, value, timestamp) VALUES (%s, %s, %s)",
            (sensor_type, value, timestamp)
        )
        conn.commit()  # Asegurarse de hacer commit sólo si la inserción es exitosa
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        conn.rollback()  # En caso de error, hacer rollback

cursor.close()
conn.close()