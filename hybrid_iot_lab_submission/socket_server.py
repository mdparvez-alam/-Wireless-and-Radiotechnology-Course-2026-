import socket

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024


def main() -> None:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Waiting for sensor connection on {HOST}:{PORT} ...")

    conn, addr = server.accept()
    print("Connected:", addr)

    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print("Sensor disconnected.")
                break

            print("Sensor data:", data.decode().strip())
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    finally:
        conn.close()
        server.close()


if __name__ == "__main__":
    main()
