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