import socket

import paho.mqtt.client as mqtt

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024

BROKER = "broker.emqx.io"
MQTT_PORT = 1883
TOPIC = "savonia/iot/temperature"


def main() -> None:
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.connect(BROKER, MQTT_PORT)
    mqtt_client.loop_start()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print("Edge device waiting for sensor...")
    print(f"Socket server listening on {HOST}:{PORT}")
    print(f"MQTT topic: {TOPIC}")

    conn, addr = server.accept()
    print("Sensor connected:", addr)

    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print("Sensor disconnected.")
                break

            value = data.decode().strip()
            print("Edge received:", value)
            mqtt_client.publish(TOPIC, value)
            print("Forwarded to MQTT:", value)
    except KeyboardInterrupt:
        print("\nEdge device stopped by user.")
    finally:
        conn.close()
        server.close()
        mqtt_client.loop_stop()
        mqtt_client.disconnect()


if __name__ == "__main__":
    main()
