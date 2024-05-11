import random
from datetime import datetime

current_temperature = 22.0
current_humidity = 50.0
current_light = 500
current_air_quality = 250
current_sound = 80
current_water = 0
current_motion = 0
current_door_window = 0

def simulate_temperature():
    global current_temperature
    current_temperature += random.uniform(-0.5, 0.5)  # Variación pequeña
    return round(max(min(current_temperature, 30), 15), 2)

def simulate_humidity():
    global current_humidity
    current_humidity += random.uniform(-1, 1)
    return round(max(min(current_humidity, 90), 30), 2)

def simulate_light():
    global current_light
    current_light += random.randint(-10, 10)
    return max(min(current_light, 1000), 100)

def simulate_air_quality():
    global current_air_quality
    current_air_quality += random.randint(-5, 5)
    return max(min(current_air_quality, 500), 0)

def simulate_sound():
    global current_sound
    current_sound += random.randint(-2, 2)
    return max(min(current_sound, 130), 30)

def simulate_motion():
    global current_motion
    # Supongamos que el movimiento es menos frecuente
    current_motion = 1 if random.random() < 0.05 else 0
    return current_motion

def simulate_water():
    global current_water
    # Supongamos que la detección de agua cambia raramente
    current_water = 1 if random.random() < 0.01 else 0
    return current_water

def simulate_door_window():
    global current_door_window
    # Cambio raro
    current_door_window = 1 if random.random() < 0.02 else 0
    return current_door_window

def generate_sensor_data(sensor_type):
    sensor_simulators = {
        'Temperature': simulate_temperature,
        'Motion': simulate_motion,
        'Light': simulate_light,
        'Humidity': simulate_humidity,
        'AirQuality': simulate_air_quality,
        'Sound': simulate_sound,
        'Water': simulate_water,
        'DoorWindow': simulate_door_window,
    }
    
    value = sensor_simulators[sensor_type]()
    return {
        'sensorId': f"{sensor_type.lower()}-{random.randint(1, 100)}",
        'type': sensor_type,
        'value': value,
        'timestamp': datetime.now().isoformat()
    }
