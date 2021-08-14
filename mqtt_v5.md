# Protocol support

There are several versions of the MQTT protocol currently standardized.
Below is a list containing the more recent versions of the MQTT protocol,
with the organization that standardized them:

- MQTT-SN v1.2, standardized by IBM
- MQTT v3.1, standardized by Eurotech and IBM
- MQTT v3.1.1, standardized by OASIS
- MQTT v5.0, standardized by OASIS

In 2019, OASIS released the official MQTT 5.0 standard.
Version 5.0 includes the following major new features:

- reason codes: acknowledgements now support return codes, which provide a reason for a failure
- shared subscriptions: allow the load to be balanced across clients and thus reduce the risk of load problems
- message expiry: messages can include an expiry date and are deleted if they are not delivered within this time period
- topic alias: the name of a topic can be replaced with a single number

