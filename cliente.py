import paho.mqtt.client as mqtt
import random
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Defina o endereço do seu broker e as credenciais fornecidas
broker = os.getenv("hive_server") 
port = 8883  
username = os.getenv("user") # Usuário fornecido pelo HiveMQ
password = os.getenv("password")  # Senha fornecida pelo HiveMQ

# Função chamada quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código de retorno: {rc}")

# Função para publicar a temperatura
def publish_temperature():
    while True:
        # Simula um valor de temperatura
        temperature = random.uniform(10.0, 40.0)
        print(f"Publicando temperatura: {temperature}")
        client.publish("meuprojeto/sensors/temperature", str(temperature))
        time.sleep(5)  # Publica a cada 5 segundos

# Criando o cliente MQTT
client = mqtt.Client()
client.username_pw_set(username, password)  # Autenticação
client.tls_set()  # Ativa TLS (para conexão segura)

# Defina as funções de callback
client.on_connect = on_connect

# Conecte ao broker
client.connect(broker, port, 60)

# Inicie a publicação de temperatura
publish_temperature()