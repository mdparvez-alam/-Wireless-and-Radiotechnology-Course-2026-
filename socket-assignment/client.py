import socket
import random
import time

HOST = "127.0.0.1"   # Server address
PORT = 5000          # Must match the server port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print(f"[CONNECTED] Connected to server at {HOST}:{PORT}")

    while True:
        temperature = round(random.uniform(20.0, 35.0), 1)
        message = f"Temperature: {temperature} C"

        client_socket.send(message.encode("utf-8"))
        print(f"[SENT] {message}")

        time.sleep(5)

except ConnectionRefusedError:
    print("[ERROR] Could not connect to the server. Make sure server.py is running first.")

except KeyboardInterrupt:
    print("\n[STOPPED] Client stopped manually.")

finally:
    client_socket.close()
    print("[CLOSED] Client socket closed.")