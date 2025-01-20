import paho.mqtt.client as mqtt
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
    # Assinando o tópico de alertas
    client.subscribe("meuprojeto/alerts/temperature")

# Função chamada quando uma mensagem de alerta é recebida
def on_alert_received(client, userdata, msg):
    print(f"Alerta recebido: {msg.payload.decode()}")

# Criando o cliente MQTT
client = mqtt.Client()
client.username_pw_set(username, password)  # Autenticação
client.tls_set()  # Ativa TLS (para conexão segura)

# Defina as funções de callback
client.on_connect = on_connect
client.on_message = on_alert_received

# Conectar ao broker e assinar o tópico de alertas
client.connect(broker, port, 60)

# Loop de recepção de alertas
client.loop_forever()