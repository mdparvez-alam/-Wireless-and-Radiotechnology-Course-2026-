import socket

HOST = "127.0.0.1"   # Localhost
PORT = 5000          # You can use another free port if needed

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")
print("[WAITING] Waiting for a client connection...")

conn, addr = server_socket.accept()
print(f"[CONNECTED] Client connected from {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            print("[DISCONNECTED] Client disconnected.")
            break

        message = data.decode("utf-8")
        print(f"[RECEIVED] {message}")

except KeyboardInterrupt:
    print("\n[STOPPED] Server stopped manually.")

finally:
    conn.close()
    server_socket.close()
    print("[CLOSED] Server socket closed.")