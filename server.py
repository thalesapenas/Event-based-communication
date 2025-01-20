import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import json

load_dotenv()


broker = os.getenv("hive_server") 
port = 8883  
username = os.getenv("user") 
password = os.getenv("password") 



TEMPERATURE_MIN = 15.0
TEMPERATURE_MAX = 30.0


def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código de retorno: {rc}")

    client.subscribe("meuprojeto/sensors/temperature")


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    temperature = payload.get("temperature")
    sensor_id = payload.get("id")
    print(f"{sensor_id}: {temperature}")

    
    if temperature < TEMPERATURE_MIN or temperature > TEMPERATURE_MAX:
        print("ALERTA: Temperatura fora do intervalo!")
        
        client.publish("meuprojeto/alerts/temperature", f"{sensor_id}: {temperature}")
    else:
        print("Temperatura dentro do intervalo.")
        
client = mqtt.Client()
client.username_pw_set(username, password)  # Autenticação
client.tls_set()  #TLS (para conexão segura)


client.on_connect = on_connect
client.on_message = on_message


client.connect(broker, port, 60)


client.loop_forever()
