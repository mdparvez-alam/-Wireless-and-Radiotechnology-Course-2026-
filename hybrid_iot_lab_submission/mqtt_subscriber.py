import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "savonia/iot/temperature"


def on_connect(client: mqtt.Client, userdata, flags, reason_code, properties=None) -> None:
    print(f"Connected to MQTT broker with result code: {reason_code}")
    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage) -> None:
    value = msg.payload.decode()
    print("Cloud received:", value)


def main() -> None:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT)
    client.loop_forever()


if __name__ == "__main__":
    main()
