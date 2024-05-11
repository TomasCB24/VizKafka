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

sensor_types = ['Temperature', 'Motion', 'Light', 'Humidity', 'AirQuality', 'Sound', 'Water', 'DoorWindow']
sensor_topics = [f'sensor-{sensor_type.lower()}' for sensor_type in sensor_types]
consumer = KafkaConsumer(
    *sensor_topics,
    bootstrap_servers=['localhost:29092', 'localhost:39092','localhost:49092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Procesar mensajes
for message in consumer:
    data = message.value
    sensor_type = data['type'].lower()
    value = data['value']
    timestamp = data['timestamp']

    table_name = f"sensor_{sensor_type}"  # Generar nombre de la tabla dinámicamente
    print(f"Recibido de {message.topic}: {data}")

    try:
        # Verificar si la tabla existe, si no, crearla
        cursor.execute(f"SELECT to_regclass('{table_name}')")
        if cursor.fetchone()[0] is None:
            cursor.execute(
                f"CREATE TABLE {table_name} (sensor_id TEXT NOT NULL, value DOUBLE PRECISION NOT NULL, timestamp TIMESTAMPTZ NOT NULL)"
            )
            cursor.execute(
                f"SELECT create_hypertable('{table_name}', 'timestamp')"
            )
            conn.commit()

        # Insertar datos en la tabla respectiva
        cursor.execute(
            f"INSERT INTO {table_name} (sensor_id, value, timestamp) VALUES (%s, %s, %s)",
            (data['sensorId'], value, timestamp)
        )
        conn.commit()  # Hacer commit si la inserción es exitosa
    except Exception as e:
        print(f"Error al insertar datos en {table_name}: {e}")
        conn.rollback()  # Hacer rollback en caso de error

cursor.close()
conn.close()