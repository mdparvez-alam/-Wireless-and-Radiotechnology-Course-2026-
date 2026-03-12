import socket

# Replace with your Bluetooth MAC address (for example, XX:XX:XX:XX:XX:XX)
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Bind to a specific Bluetooth device (change the MAC address) and port 4
server.bind(("XX:XX:XX:XX:XX:XX", 4))

server.listen(1)  # Wait for 1 connection
print("Waiting for Bluetooth client connection...")

client, addr = server.accept()
print(f"Connected to: {addr}")

try:
    while True:
        data = client.recv(1024)  # Receive data from the client (sensor)
        if not data:
            break  # Exit if no data is received
        print("Received:", data.decode("utf-8"))  # Decode and print received data

except OSError:
    pass  # Handle any Bluetooth socket errors

client.close()  # Close the connection
server.close()  # Close the server socket