# Quality of service (QoS)

Quality of service refers to traffic prioritization and resource reservation
control mechanisms rather than the achieved service quality. Quality of
service is the ability to provide different priority to different applications,
users, or data flows, or to guarantee a certain level of performance to a data
flow.

Each connection to the broker can specify a quality of service measure.
These are classified in increasing order of overhead:

- at most once - the message is sent only once and the client and broker take
no additional steps to acknowledge delivery (fire and forget)

- at least once - the message is re-tried by the sender multiple times until
acknowledgement is received (acknowledged delivery)

- exactly once - the sender and receiver engage in a two-level handshake to
ensure only one copy of the message is received (assured delivery)

This field does not affect handling of the underlying TCP data transmissions;
it is only used between MQTT senders and receivers.

### Last Will And Testament

MQTT clients can register a custom “last will and testament” message to be
sent by the broker if they disconnect. These messages can be used to signal
to subscribers when a device disconnects.

### Persistence

MQTT has support for persistent messages stored on the broker. When publishing
messages, clients may request that the broker persists the message. Only the
most recent persistent message is stored. When a client subscribes to a topic,
any persisted message will be sent to the client.

Unlike a message queue, MQTT brokers do not allow persisted messages to back
up inside the server.

### Security

MQTT brokers may require username and password authentication from clients
to connect. To ensure privacy, the TCP connection may be encrypted with SSL/TLS.

### MQTT-SN

Even though MQTT is designed to be lightweight, it has two drawbacks for very
constrained devices.

Every MQTT client must support TCP and will typically hold a connection open
to the broker at all times. For some environments where packet loss is high
or computing resources are scarce, this is a problem.

MQTT topic names are often long strings which make them impractical for 802.15.4.

Both of these shortcomings are addressed by the MQTT-SN protocol, which defines
a UDP mapping of MQTT and adds broker support for indexing topic names.

