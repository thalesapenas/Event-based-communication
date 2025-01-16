# Projeto: Sistema de Monitoramento de Sensores com MQTT

## **Descrição do Projeto**
Este projeto é um sistema distribuído para monitoramento de sensores utilizando o protocolo MQTT, uma solução leve e eficiente para comunicação baseada em eventos. Ele é composto por três componentes principais:

1. **Sensores (Clientes)**: Publicam leituras de temperatura em um tópico MQTT.
2. **Servidor de Validação**: Valida os dados recebidos dos sensores e verifica se estão dentro de um intervalo definido.
3. **Clientes de Alerta**: Monitoram os tópicos de alerta e notificam em caso de anomalias.

### **Problema Resolvido**
O sistema aborda o problema de validação e monitoramento de dados em tempo real provenientes de sensores distribuídos. Caso um sensor reporte um valor fora do intervalo esperado, um alerta é gerado e enviado para dispositivos ou sistemas que possam tomar ação apropriada. No entanto, para fins de representação do funcionamento da solução, utilizaremos dados provenientes de APIs de temperaturas. 

### **Arquitetura do Sistema**
- **Broker MQTT na Nuvem**: Utiliza o HiveMQ Cloud para gerenciar a comunicação entre sensores, servidor e clientes de alerta.
- **Publicação/Assinatura**: Sensores publicam leituras, enquanto o servidor e os clientes de alerta assinam os tópicos relevantes.
- **Validação Dinâmica**: O servidor de validação analisa as leituras em tempo real e emite alertas conforme necessário.

---

## **Como Usar o Sistema**

### **1. Configuração do Broker MQTT na Nuvem (HiveMQ Cloud)**

1. Crie uma conta no [HiveMQ Cloud](https://www.hivemq.com/mqtt-cloud/).
2. Configure um novo broker e anote as informações:
   - Endereço do broker (exemplo: `xxxxxx.hivemq.cloud`)
   - Porta segura (normalmente `8883`)
   - Nome de usuário
   - Senha
3. Ative o suporte a TLS para conexões seguras.

### **2. Requisitos de Software**
- Python 3.7 ou superior.
- Biblioteca Paho MQTT: Instale usando o comando:
  ```bash
  pip install paho-mqtt
  ```

### **3. Clonar o Repositório**
Clone o repositório para sua máquina local:
```bash
git clone https://github.com/seu-usuario/Event-based-communication.git
cd mqtt-validation-project
```

### **4. Configuração dos Códigos**
Edite os seguintes arquivos para incluir suas credenciais do HiveMQ:
- **`sensor.py`**: Configurar `broker`, `username` e `password`.
- **`validator_server.py`**: Configurar `broker`, `username` e `password`.
- **`alert_client.py`**: Configurar `broker`, `username` e `password`.

### **5. Executar os Componentes**

#### **Passo 1: Inicie o Sensor (Cliente)**
Este componente publica dados simulados de temperatura.
```bash
python sensor.py
```

#### **Passo 2: Inicie o Servidor de Validação**
Este componente recebe os dados dos sensores, valida-os e publica alertas caso haja anomalias.
```bash
python validator_server.py
```

#### **Passo 3: Inicie o Cliente de Alerta**
Este componente escuta os alertas e exibe notificações de temperatura fora do intervalo esperado.
```bash
python alert_client.py
```

---

## **Funcionamento do Sistema**

1. O **sensor** publica valores de temperatura no tópico `meuprojeto/sensors/temperature` a cada 5 segundos.
2. O **servidor de validação**:
   - Recebe os valores publicados.
   - Valida se estão dentro do intervalo (15°C a 30°C, por padrão).
   - Publica alertas no tópico `meuprojeto/alerts/temperature` caso o valor esteja fora do intervalo.
3. O **cliente de alerta**:
   - Monitora o tópico `meuprojeto/alerts/temperature`.
   - Exibe alertas em tempo real para notificar problemas.

---

## **Exemplo de Saída**

### **Sensor (sensor.py)**
```plaintext
Publicando temperatura: 18.45
Publicando temperatura: 31.87
Publicando temperatura: 14.22
```

### **Servidor de Validação (validator_server.py)**
```plaintext
Temperatura recebida: 18.45
Temperatura dentro do intervalo.
Temperatura recebida: 31.87
ALERTA: Temperatura fora do intervalo!
Temperatura recebida: 14.22
ALERTA: Temperatura fora do intervalo!
```

### **Cliente de Alerta (alert_client.py)**
```plaintext
Alerta recebido: ALERTA: Temperatura fora do intervalo! Valor: 31.87
Alerta recebido: ALERTA: Temperatura fora do intervalo! Valor: 14.22
```

---

## **Personalização**

- **Intervalo de Temperatura**: Altere as variáveis `TEMPERATURE_MIN` e `TEMPERATURE_MAX` no arquivo `validator_server.py`.
- **Tópicos**: Atualize os tópicos MQTT nos arquivos para refletir a estrutura do seu projeto.

---

## **Considerações Finais**

Este projeto é uma solução modular e escalável para monitoramento de sensores distribuídos. Com ele, é possível integrar diversos sensores, validar dados em tempo real e enviar notificações de forma eficiente. Utilize-o como base para criar sistemas mais complexos ou adaptá-lo às suas necessidades.

Se tiver dúvidas ou sugestões, entre em contato!

