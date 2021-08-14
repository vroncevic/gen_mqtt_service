Quality of service (QoS)

From the MQTT page, quality of service (QoS) is described as,

Quality of service refers to traffic prioritization and resource reservation control mechanisms rather than the achieved service quality. Quality of service is the ability to provide different priority to different applications, users, or data flows, or to guarantee a certain level of performance to a data flow.


Each connection to the broker can specify a quality of service measure. These are classified in increasing order of overhead:

At most once - the message is sent only once and the client and broker take no additional steps to acknowledge delivery (fire and forget).
At least once - the message is re-tried by the sender multiple times until acknowledgement is received (acknowledged delivery).
Exactly once - the sender and receiver engage in a two-level handshake to ensure only one copy of the message is received (assured delivery).
[23] This field does not affect handling of the underlying TCP data transmissions; it is only used between MQTT senders and receivers.
