# MQTT temperature service

For example, imagine a simple network with three clients and a central broker.

All three clients open TCP connections with the broker. Clients B and C
subscribe to the topic temperature.

![MQTT subscribe](https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/mqtt_temperature_service_subscribe.png)

At a later time, Client A publishes a value of 22.5 for topic temperature .
The broker forwards the message to all subscribed clients.

![MQTT publish](https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/mqtt_temperature_service_publish.png)

The publisher subscriber model allows MQTT clients to communicate one-to-one,
one-to-many and many-to-one.

### Scaffolding this architecture with gen_mqtt_service

You can scaffold this exact publisher/subscriber topology in your language of choice:

#### 1. Python (Paho) Implementation
```bash
# Generate temperature service demo
python3 main.py create --name temp_service --type paho --role both --scope demo --output ./services/

# Start subscriber (Clients B & C)
cd ./services/temp_service && bash run_subscriber.sh

# Publish temperature readings (Client A)
cd ./services/temp_service && bash run_publisher.sh
```

#### 2. C (Mosquitto) Implementation
```bash
# Generate C service demo
python3 main.py create --name temp_c --type mosquitto --role both --scope demo --output ./services/

# Build and run
cd ./services/temp_c && make
./build/subscriber &
./build/publisher
```

#### 3. Node.js Implementation
```bash
# Generate Node.js service demo
python3 main.py create --name temp_node --type node --role both --scope demo --output ./services/

# Install and run
cd ./services/temp_node && npm install
bash run_subscriber.sh &
bash run_publisher.sh
```

For complete technical details on project layouts, factories, and architectural patterns, see the [Templates Architecture & Usage Guide](templates_guide.md).