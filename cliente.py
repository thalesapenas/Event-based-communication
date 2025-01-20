import paho.mqtt.client as mqtt
import random
import time
from dotenv import load_dotenv
import os
import json

load_dotenv()


broker = os.getenv("hive_server") 
port = 8883  
username = os.getenv("user") 
password = os.getenv("password") 
TOPIC = "meuprojeto/sensors/temperature"
SENSOR_ID = "sensor_02"


def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código de retorno: {rc}")


def publish_temperature():
    while True:
        
        temperature = random.uniform(10.0, 40.0)
        payload = {
            "id": SENSOR_ID,
            "temperature": temperature
        }
        client.publish(TOPIC, json.dumps(payload))
        print(f"Publicado: {payload}")
        time.sleep(5)  


client = mqtt.Client()
client.username_pw_set(username, password)  # Autenticação
client.tls_set()  #TLS (para conexão segura)


client.on_connect = on_connect


client.connect(broker, port, 60)


publish_temperature()
