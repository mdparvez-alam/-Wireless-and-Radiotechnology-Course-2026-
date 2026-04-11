import random
import socket
import time
from datetime import datetime

# -------------------------------
# Laptop 1 (Sensor)
# Sends simulated temperature data to Laptop 2 using TCP sockets.
# -------------------------------

# Change this to the IP address of Laptop 2
EDGE_DEVICE_IP = "127.0.0.1"
EDGE_DEVICE_PORT = 5000
SEND_INTERVAL_SECONDS = 2


def generate_temperature() -> float:
    """Generate a realistic demo temperature value."""
    return round(random.uniform(20.0, 35.0), 2)


def main() -> None:
    print("Starting socket sensor...")
    print(f"Target edge device: {EDGE_DEVICE_IP}:{EDGE_DEVICE_PORT}")

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((EDGE_DEVICE_IP, EDGE_DEVICE_PORT))
                print("Connected to edge device. Sending data...\n")

                while True:
                    temperature = generate_temperature()
                    message = f"{temperature}\n"
                    client.sendall(message.encode("utf-8"))

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{timestamp}] Sent temperature: {temperature} °C")
                    time.sleep(SEND_INTERVAL_SECONDS)

        except (ConnectionRefusedError, ConnectionResetError, OSError) as exc:
            print(f"Connection problem: {exc}")
            print("Retrying in 3 seconds...\n")
            time.sleep(3)


if __name__ == "__main__":
    main()
