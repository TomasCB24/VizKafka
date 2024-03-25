import random
from datetime import datetime

def simulate_temperature():
    """Simula datos de un sensor de temperatura, en grados Celsius."""
    return round(random.uniform(15, 30), 2)

def simulate_motion():
    """Simula datos de un sensor de movimiento (0: no hay movimiento, 1: movimiento detectado)."""
    return random.choice([0, 1])

def simulate_light():
    """Simula datos de un sensor de luz, en lúmenes."""
    return random.randint(100, 1000)

def simulate_humidity():
    """Simula datos de un sensor de humedad, en porcentaje."""
    return round(random.uniform(30, 90), 2)

def simulate_air_quality():
    """Simula datos de un sensor de calidad del aire, índice de calidad (cuanto menor, mejor)."""
    return random.randint(0, 500)

def simulate_sound():
    """Simula datos de un sensor de sonido, en decibelios."""
    return random.randint(30, 130)

def simulate_water():
    """Simula datos de un sensor de agua (0: seco, 1: agua detectada)."""
    return random.choice([0, 1])

def simulate_door_window():
    """Simula datos de un sensor de puerta/ventana (0: cerrado, 1: abierto)."""
    return random.choice([0, 1])

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
