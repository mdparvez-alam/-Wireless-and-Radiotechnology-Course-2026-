import socket
import random
import time

# Replace with the server's Bluetooth MAC address (for example, XX:XX:XX:XX:XX:XX)
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("XX:XX:XX:XX:XX:XX", 4))  # Connect to the server's MAC address and port 4

print("Connected to Bluetooth server")

try:
    while True:
        # Generate a random temperature between 20°C to 30°C
        temperature = round(random.uniform(20.0, 30.0), 1)
        message = f"Temperature: {temperature} C"  # Create the message with the temperature data
        
        # Send the message to the server
        client.send(message.encode("utf-8"))
        print("Sent:", message)

        time.sleep(5)  # Wait for 5 seconds before sending the next data

except OSError:
    pass  # Handle any Bluetooth socket errors

client.close()  # Close the client connection