import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Defina o endereço do seu broker e as credenciais fornecidas
broker = os.getenv("hive_server") 
port = 8883  
username = os.getenv("user") # Usuário fornecido pelo HiveMQ
password = os.getenv("password")  # Senha fornecida pelo HiveMQ


# Intervalo esperado para a temperatura (exemplo: 15°C a 30°C)
TEMPERATURE_MIN = 15.0
TEMPERATURE_MAX = 30.0

# Função chamada quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    print(f"Conectado com o código de retorno: {rc}")
    # Assinando o tópico onde os sensores publicam dados
    client.subscribe("meuprojeto/sensors/temperature")

# Função chamada quando uma mensagem é recebida em um tópico
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    temperature = payload.get("temperature")
    sensor_id = payload.get("id")
    print(f"{sensor_id}: {temperature}")

    # Validação da temperatura
    if temperature < TEMPERATURE_MIN or temperature > TEMPERATURE_MAX:
        print("ALERTA: Temperatura fora do intervalo!")
        # Envia uma mensagem de alerta em um tópico de alerta
        client.publish("meuprojeto/alerts/temperature", f"{sensor_id}: {temperature}")
    else:
        print("Temperatura dentro do intervalo.")

# Criando o cliente MQTT
client = mqtt.Client()
client.username_pw_set(username, password)  # Autenticação
client.tls_set()  # Ativa TLS (para conexão segura)

# Defina as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect(broker, port, 60)

# Loop de recebimento de mensagens
client.loop_forever()