# Templates Architecture & Usage Guide

`gen_mqtt_service` scaffolds complete MQTT client skeletons across multiple programming languages and runtime environments. Each template is engineered according to best architectural practices, from strict SOLID principles in Python to high-performance C11 and event-driven Node.js.

---

## Supported Template Types

| Template Type | Language / Platform | Transport | Primary Library | Architecture Pattern |
|---|---|---|---|---|
| `paho` | Python 3.10+ | TCP | `paho-mqtt` | SOLID, Protocol-based DIP, Factory Pattern |
| `mosquitto` | C (C11) | TCP | `libmosquitto` | Modular C11, Typed Constants, CMake / Make |
| `node` | JavaScript (Node.js) | TCP | `mqtt` (NPM) | Asynchronous Event-Driven |
| `node_ws` | JavaScript (Node.js) | WebSockets / TCP | `mqtt`, `aedes`, `ws` | WebSocket MQTT with Embedded Broker |

---

## Generation Options

When running `gen_mqtt_service create`, you can fine-tune what components are generated using `--role` and `--scope`:

```bash
gen_mqtt_service create --name <NAME> --type <TYPE> --output <DIR> [--role <ROLE>] [--scope <SCOPE>]
```

### 1. Role Matrix (`--role`)

Controls the operational roles included in the generated project:

* **`both`** *(default)*: Generates both **Publisher** and **Subscriber** components, along with shared connection infrastructure.
* **`publisher`**: Generates only the **Publisher** component (and common connection modules). Excludes subscriber code.
* **`subscriber`**: Generates only the **Subscriber** component (and common connection modules). Excludes publisher code.

### 2. Scope Matrix (`--scope`)

Controls whether you get a ready-to-run standalone demo or clean library modules to embed in existing systems:

* **`demo`** *(default)*: Generates complete runnable scaffolding, including entry point scripts (`main.py`, `publisher.c`, `server.js`, etc.), shell runners (`run_publisher.sh`, `run_subscriber.sh`), build configurations (`Makefile`, `CMakeLists.txt`, `package.json`, `pyproject.toml`, `requirements.txt`), and documentation.
* **`module`**: Strips out all scaffolding and runner scripts, generating only the pure reusable source modules. Ideal when embedding MQTT capabilities into an existing codebase.

---

## Detailed Template Architectures

### 1. Python Paho (`paho`)

The `paho` template is designed around **Clean Architecture**, **Dependency Inversion (DIP)**, and **Single Responsibility (SRP)**.

#### Directory Structure (`--scope demo --role both`)

```text
<project_name>/
├── common/
│   ├── imqtt_client.py           # Protocol: IMqttClient interface (PEP 544)
│   ├── mqtt_client.py            # Concrete MqttClient (wraps paho.mqtt.client)
│   └── mqtt_bundle.py            # Connection config value object / dataclass
├── publisher/
│   ├── imqtt_publisher.py        # Protocol: IMqttPublisher interface
│   ├── mqtt_publisher.py         # Domain publisher implementation
│   ├── mqtt_publisher_factory.py # Factory creating wired publisher instances
│   └── main.py                   # Standalone publisher CLI entry point
├── subscriber/
│   ├── imqtt_subscriber.py       # Protocol: IMqttSubscriber interface
│   ├── imqtt_message_handler.py  # Protocol: IMqttMessageHandler interface
│   ├── mqtt_message_handler.py   # Concrete payload / topic handler
│   ├── mqtt_subscriber.py        # Domain subscriber implementation
│   ├── mqtt_subscriber_factory.py# Factory creating wired subscriber instances
│   └── main.py                   # Standalone subscriber CLI entry point
├── pyproject.toml                # Project metadata and type checker path config
├── requirements.txt              # Dependencies (paho-mqtt)
├── README.md                     # Project documentation
├── run_publisher.sh              # Publisher start script
└── run_subscriber.sh             # Subscriber start script
```

#### Key Design Highlights
* **Structural Protocol Typing**: All interfaces are defined using `@runtime_checkable` `typing.Protocol`. Concrete implementations do **not** inherit from or import protocols, avoiding circular imports and tight coupling.
* **Dependency Inversion**: Neither `MqttPublisher` nor `MqttSubscriber` imports or depends on the third-party `paho` library. They depend strictly on `IMqttClient` and `IMqttMessageHandler`.
* **Clean Factories**: `MqttPublisherFactory` and `MqttSubscriberFactory` encapsulate the composition root, instantiating `MqttClient` and wiring it into the publishers and subscribers.
* **Standalone IDE Support**: Includes `pyproject.toml` with `[tool.pyright] extraPaths = ["."]` so linters and language servers resolve imports immediately upon opening the project folder.

#### Running the Python Demo
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. In terminal A: Start subscriber
bash run_subscriber.sh

# 3. In terminal B: Publish messages
bash run_publisher.sh
```

---

### 2. C Mosquitto (`mosquitto`)

The `mosquitto` template provides high-performance, memory-safe C11 code linking against `libmosquitto`.

#### Directory Structure (`--scope demo --role both`)

```text
<project_name>/
├── CMakeLists.txt     # Modern CMake build definition
├── Makefile           # Convenience makefile wrapping CMake
├── publisher.c        # Standalone C publisher
├── subscriber.c       # Standalone C subscriber
└── README.md          # Build and run instructions
```

#### Key Design Highlights
* **Modern C11 Standards**: Pure C11 compliant, avoiding deprecated constructs.
* **Type-Safe Constants**: All connection options, QoS levels, and buffer limits are declared using strongly typed `static const` variables instead of brittle `#define` preprocessor macros.
* **Memory & Buffer Safety**: Bounded string operations (`snprintf`) and explicit unused parameter suppressions ensure 0 compiler warnings under `-Wall -Wextra -Wpedantic`.

#### Building and Running the C Demo
```bash
# Prerequisites (Debian/Ubuntu)
sudo apt-get install -y build-essential cmake libmosquitto-dev

# 1. Build using Makefile or CMake
make

# 2. In terminal A: Run subscriber
./build/subscriber

# 3. In terminal B: Run publisher
./build/publisher
```

---

### 3. Node.js Standard MQTT (`node`)

The `node` template offers an asynchronous, event-driven MQTT client designed for Node.js environments.

#### Directory Structure (`--scope demo --role both`)

```text
<project_name>/
├── package.json       # Node.js dependencies (mqtt) and run scripts
├── publisher.js       # Asynchronous MQTT publisher
├── subscriber.js      # Asynchronous MQTT subscriber
├── README.md          # Instructions
├── run_publisher.sh   # Bash wrapper to run npm run publish
└── run_subscriber.sh  # Bash wrapper to run npm run subscribe
```

#### Key Design Highlights
* **Event-Driven Architecture**: Hooks into native MQTT events (`connect`, `message`, `error`, `close`, `reconnect`).
* **Clean Configuration**: Centralized broker URL (`mqtt://localhost:1883`), topic, and options object.
* **QoS Support**: Configurable Quality of Service (QoS 0, 1, 2) and retain flag.

#### Running the Node.js Demo
```bash
# 1. Install dependencies
npm install

# 2. In terminal A: Run subscriber
bash run_subscriber.sh
# or: npm run subscribe

# 3. In terminal B: Run publisher
bash run_publisher.sh
# or: npm run publish
```

---

### 4. Node.js WebSocket MQTT with Embedded Broker (`node_ws`)

The `node_ws` template is designed for browser-compatible WebSockets and self-contained deployments.

#### Directory Structure (`--scope demo --role both`)

```text
<project_name>/
├── package.json       # Dependencies (mqtt, ws, aedes, aedes-server-factory)
├── server.js          # Embedded Aedes MQTT broker (WebSocket + TCP)
├── publisher.js       # WebSocket MQTT publisher
├── subscriber.js      # WebSocket MQTT subscriber
├── README.md          # Instructions
├── run_publisher.sh   # Bash wrapper to run npm run publish
└── run_subscriber.sh  # Bash wrapper to run npm run subscribe
```

#### Key Design Highlights
* **Embedded Aedes Broker**: `server.js` starts a lightweight, embedded MQTT broker listening on:
  * **WebSocket port 8080** (`ws://localhost:8080`)
  * **Standard TCP port 1883** (`mqtt://localhost:1883`)
* **Browser Ready**: Enables web applications and hybrid clients to publish and subscribe directly over WebSockets without needing proxy software.
* **Zero External Dependencies**: Does not require an external broker like Mosquitto to be installed, making it instantly runnable.

#### Running the Node.js WebSocket Demo
```bash
# 1. Install dependencies
npm install

# 2. In terminal A: Start embedded broker
node server.js

# 3. In terminal B: Run subscriber
bash run_subscriber.sh

# 4. In terminal C: Run publisher
bash run_publisher.sh
```

---

## Integration Guide: Embedding as Module (`--scope module`)

When you specify `--scope module`, `gen_mqtt_service` generates strictly the business and transport modules, allowing seamless integration into existing applications.

### Example: Embedding Python `paho` into an Existing Application

1. Generate the module:
   ```bash
   gen_mqtt_service create --name telemetry --type paho --role both --scope module --output ./my_app/
   ```
2. Your project structure:
   ```text
   my_app/
   └── telemetry/
       ├── common/
       │   ├── imqtt_client.py
       │   ├── mqtt_client.py
       │   └── mqtt_bundle.py
       ├── publisher/
       │   ├── imqtt_publisher.py
       │   ├── mqtt_publisher.py
       │   └── mqtt_publisher_factory.py
       └── subscriber/
           ├── imqtt_subscriber.py
           ├── imqtt_message_handler.py
           ├── mqtt_message_handler.py
           ├── mqtt_subscriber.py
           └── mqtt_subscriber_factory.py
   ```
3. Use it directly in your application code:
   ```python
   from my_app.telemetry.common.mqtt_bundle import MqttBundle
   from my_app.telemetry.publisher.mqtt_publisher_factory import MqttPublisherFactory

   bundle = MqttBundle(
       host="mqtt.internal.net",
       port=1883,
       keepalive=60,
       username="sensor_user",
       password="secret_password"
   )

   publisher = MqttPublisherFactory.create(bundle)
   publisher.publish(topic="sensors/temperature", payload="21.5", qos=1)
   publisher.disconnect()
   ```

---

## Summary Matrix

| Need / Use Case | Recommended Command |
|---|---|
| Python microservice / backend service | `gen_mqtt_service create --name svc --type paho --role both --scope module --output ./` |
| Python quick demo & testing | `gen_mqtt_service create --name demo --type paho --role both --scope demo --output ./` |
| Embedded C / IoT firmware publisher | `gen_mqtt_service create --name iot_node --type mosquitto --role publisher --scope demo --output ./` |
| Node.js backend listener / ingestion service | `gen_mqtt_service create --name ingest --type node --role subscriber --scope demo --output ./` |
| Web front-end or browser-accessible MQTT | `gen_mqtt_service create --name web_mqtt --type node_ws --role both --scope demo --output ./` |
