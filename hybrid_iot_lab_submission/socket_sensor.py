import random
import socket
import time

# Replace this with the real IP address of Laptop 2 (edge device / socket server)
SERVER_IP = "192.168.x.x"
PORT = 5000
SEND_INTERVAL_SECONDS = 5


def main() -> None:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    print(f"Connected to edge device at {SERVER_IP}:{PORT}")

    try:
        while True:
            temperature = round(random.uniform(20, 35), 2)
            message = f"{temperature}"
            client.send(message.encode())
            print("Sensor value sent:", temperature)
            time.sleep(SEND_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nSensor client stopped by user.")
    finally:
        client.close()


if __name__ == "__main__":
    main()
