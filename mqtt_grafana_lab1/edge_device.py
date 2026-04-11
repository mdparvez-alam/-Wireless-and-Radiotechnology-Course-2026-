import socket
from datetime import datetime

import paho.mqtt.client as mqtt

# -------------------------------
# Laptop 2 (Edge Device)
# Receives data from Laptop 1 using TCP sockets,
# then forwards that data to an MQTT broker.
# -------------------------------

SOCKET_HOST = "0.0.0.0"
SOCKET_PORT = 5000
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "savonia/iot/temperature/adnan"


def create_mqtt_client() -> mqtt.Client:
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    return client


def handle_client(conn: socket.socket, addr: tuple[str, int], mqtt_client: mqtt.Client) -> None:
    print(f"Connected by {addr}")
    buffer = ""

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Connection closed by {addr}\n")
                break

            buffer += data.decode("utf-8")

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                value = line.strip()
                if not value:
                    continue

                mqtt_client.publish(MQTT_TOPIC, value)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Published to MQTT topic '{MQTT_TOPIC}': {value} °C")


def main() -> None:
    mqtt_client = create_mqtt_client()
    print("Starting edge device...")
    print(f"Socket server: {SOCKET_HOST}:{SOCKET_PORT}")
    print(f"MQTT broker: {MQTT_BROKER}:{MQTT_PORT}")
    print(f"MQTT topic:  {MQTT_TOPIC}\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((SOCKET_HOST, SOCKET_PORT))
        server.listen()
        print("Waiting for sensor connection...\n")

        while True:
            conn, addr = server.accept()
            handle_client(conn, addr, mqtt_client)


if __name__ == "__main__":
    main()
