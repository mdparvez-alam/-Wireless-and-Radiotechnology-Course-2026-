# Bluetooth Sensor to Gateway with Python

## Project Description
In this project, a simple Bluetooth client-server application is created in Python. The client simulates a sensor device that generates random temperature data every 5 seconds. This data is sent over Bluetooth to a gateway device (server), which receives and prints the data.

The client uses Bluetooth RFCOMM sockets to send temperature values (simulated by random data generation), and the server listens for incoming Bluetooth connections, receiving and printing the data.

## Bluetooth MAC Address Used
- **Server (Gateway) Bluetooth MAC address**: XX:XX:XX:XX:XX:XX  
  *(Replace this with your actual MAC address)*

## How to Run
### Step 1: Setup Bluetooth on both devices
- Ensure Bluetooth is enabled on both devices (client and server).
- Pair the devices via Bluetooth.
- Find the Bluetooth MAC address of the server device.

### Step 2: Running the Server
1. Run the `server.py` on the gateway device.
    ```bash
    python server.py
    ```
    The server will wait for the client to connect and display the received temperature data.

### Step 3: Running the Client
1. Run the `client.py` on the sensor device.
    ```bash
    python client.py
    ```
    The client will start sending random temperature data every 5 seconds to the server.

### Step 4: Check the Output
- The server will display the received temperature messages from the client.

## Screenshot of Successful Communication
*Insert a screenshot here showing the client sending data and the server receiving it.*

## Reflection
### What did you learn?
This project helped me understand the use of Bluetooth communication in Python using RFCOMM sockets. I also learned how to generate random sensor data and send it to another device using Bluetooth.

### What was difficult?
The most challenging part was ensuring that both devices were properly paired and setting up the correct MAC addresses for Bluetooth communication. Additionally, debugging Bluetooth connection issues was sometimes tricky.

### Where could Bluetooth communication be useful in IoT?
Bluetooth communication can be useful in IoT systems where short-range, low-power communication is needed. For example, it can be used in wearable devices, home automation systems, and health monitoring systems.

## Reflection Question: Difference between Bluetooth and WiFi socket communication in practice:
- **Bluetooth socket communication** is typically used for short-range, lower-power applications (like personal area networks - PAN). It is ideal for connecting devices within a small distance (usually up to 100 meters).
- **WiFi socket communication**, on the other hand, is more suitable for longer-range communication (typically used for connecting devices to a home or office network). It offers faster speeds and broader coverage compared to Bluetooth.

## Evaluation
You will pass if:
- Bluetooth connection works correctly between client and server
- Sensor data is sent every 5 seconds
- Server successfully receives and prints the data
- Code is uploaded to GitHub
- README file is included
