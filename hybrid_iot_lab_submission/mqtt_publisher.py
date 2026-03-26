import random
import time

import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "savonia/iot/temperature"
SEND_INTERVAL_SECONDS = 5


def main() -> None:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, PORT)
    client.loop_start()

    print(f"Connected to MQTT broker {BROKER}:{PORT}")
    print(f"Publishing to topic: {TOPIC}")

    try:
        while True:
            temperature = round(random.uniform(20, 35), 2)
            client.publish(TOPIC, temperature)
            print("Published to MQTT:", temperature)
            time.sleep(SEND_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nMQTT publisher stopped by user.")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
