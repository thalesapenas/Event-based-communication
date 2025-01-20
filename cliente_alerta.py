import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()


broker = os.getenv("hive_server") 
port = 8883  
username = os.getenv("user") 
password = os.getenv("password") 


def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código de retorno: {rc}")
  
    client.subscribe("meuprojeto/alerts/temperature")


def on_alert_received(client, userdata, msg):
    print(f"Alerta recebido: {msg.payload.decode()}")


client = mqtt.Client()
client.username_pw_set(username, password)  # Autenticação
client.tls_set()  #TLS (para conexão segura)


client.on_connect = on_connect
client.on_message = on_alert_received


client.connect(broker, port, 60)


client.loop_forever()
