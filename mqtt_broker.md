# MQTT broker

The MQTT broker is software running on a computer (running on-premises or in
the cloud), and could be self-built or hosted by a third party. It is
available in both open source and proprietary implementations.

The broker acts as a post office, MQTT doesn't use the address of the
intended recipient but uses the subject line called “Topic”, and anyone who
wants a copy of that message will subscribe to that topic. Multiple clients
can receive the [message](message_types.md) from a single broker (one to many capability).
Similarly, multiple publishers can publish topics to a single subscriber
(many to one).

Each client can both produce and receive data by both publishing and
subscribing, i.e. the devices can publish sensor data and still be able to
receive the configuration information or control commands (MQTT is a
bi-directional communication protocol). This helps in both sharing data,
managing and controlling devices.

With MQTT broker architecture, the devices and application becomes decoupled
and more secure. MQTT uses Transport Layer Security (TLS) encryption with
user name, password protected connections, and optional certifications that
requires clients to provide a certificate file that matches with the server’s.
The clients are unaware of each other's IP address.

In case of a single source of failure, broker software and clients have an
automatic handover to Redundant/automatic backup broker. The backup broker can
also be set up to share the load of clients across multiple servers onsite,
cloud, or the combination of both.

The broker can support both standard MQTT and MQTT for compliant specifications
such as Sparkplug, can be done with same server, same time and with same levels
of security.

The broker can store the data in the form of retained messages (need to
subscribe with database client) so that new subscribers to the topic can get
the last value straight away.

The broker also keeps track of all the session’s information as the devices
goes on and off called “persistent sessions”.

### Example of MQTT service for tracking temperature

![Temperature tracking based on MQTT](https://raw.githubusercontent.com/vroncevic/gen_mqtt_service/dev/docs/MQTT_protocol_example_without_QoS.png)

### Advantages

The main advantages of MQTT broker are:

- eliminates vulnerable and insecure client connections
- can easily scale from a single device to thousands
- manages and tracks all client connection states, including security credentials and certificates
- reduced network strain without compromising the security (cellular or satellite network)