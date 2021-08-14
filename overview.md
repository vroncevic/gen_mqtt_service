# The MQTT protocol

MQTT defines two types of network entities:
- message [broker](mqtt_broker.md), and
- number of clients

Mosquitto ===> Client and Broker (thread safety)
Paho MQTT ===> Client

An MQTT [broker](mqtt_broker.md) is a server that receives all messages from the clients and
then routes the messages to the appropriate destination clients. An MQTT
client is any device (from a micro controller up to a fully-fledged server)
that runs an MQTT library and connects to an MQTT [broker](mqtt_broker.md) over a network.

Information is organized in a hierarchy of topics. When a publisher has a new
item of data to distribute, it sends a control message with the data to the
connected broker. The [broker](mqtt_broker.md) then distributes the information to any clients
that have subscribed to that topic. The publisher does not need to have any
data on the number or locations of subscribers, and subscribers, in turn, do
not have to be configured with any data about the publishers.

If a broker receives a message on a topic for which there are no current
subscribers, the broker discards the message unless the publisher of the
message designated the message as a retained message. A retained message
is a normal MQTT message with the retained flag set to true. The broker
stores the last retained message and the corresponding [QoS](quality_of_service.md) for the selected
topic. Each client that subscribes to a topic pattern that matches the topic
of the retained message receives the retained message immediately after
they subscribe. The broker stores only one retained message per topic.
This allows new subscribers to a topic to receive the most current value
rather than waiting for the next update from a publisher.

When a publishing client first connects to the [broker](mqtt_broker.md), it can set up a
default message to be sent to subscribers if the broker detects that the
publishing client has unexpectedly disconnected from the broker.

Clients only interact with a [broker](mqtt_broker.md), but a system may contain several
broker servers that exchange data based on their current subscribers' topics.

A minimal MQTT control message can be as little as two bytes of data.
A control message can carry nearly 256 megabytes of data if needed.
There are fourteen defined message types used to connect and disconnect
a client from a [broker](mqtt_broker.md), to publish data, to acknowledge receipt of data,
and to supervise the connection between client and server.

MQTT relies on the TCP protocol for data transmission. A variant, MQTT-SN,
is used over other transports such as UDP or Bluetooth.

MQTT sends connection credentials in plain text format and does not include
any measures for security or authentication. This can be provided by using
TLS to encrypt and protect the transferred information against interception,
modification or forgery.

The default unencrypted MQTT port is 1883. The encrypted port is 8883.

[Protocol support](mqtt_v5.md) more details.

