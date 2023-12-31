# Message types

### Connect

Example of an MQTT connection ([QoS](quality_of_service.md) 0) with connect,
publish/subscribe, and disconnect. The first message from client B is stored
due to the retain flag. Waits for a connection to be established with the
server and creates a link between the nodes.

### Disconnect

Waits for the MQTT client to finish any work it must do, and for the TCP/IP
session to disconnect.

### Publish

Returns immediately to the application thread after passing the request to
the MQTT client.