# Lab 1 - Real-Time MQTT Monitoring with Grafana

## Student Submission
This project extends the previous IoT pipeline by adding a live monitoring dashboard in Grafana.

## 1. Short Description of the Full System
The system has two laptops:

- **Laptop 1** works as the sensor node and sends temperature data using **socket programming**.
- **Laptop 2** works as the edge device. It receives the socket data and publishes it to an **MQTT broker**.
- **Grafana on Laptop 1** connects to the same MQTT topic and displays the incoming values in real time.

So the complete flow is:

**Laptop 1 (Sensor) -> Socket -> Laptop 2 (Edge Device) -> MQTT Broker -> Grafana on Laptop 1**

---

## 2. Socket Data Flow from Laptop 1 to Laptop 2
The file `socket_sensor.py` runs on Laptop 1.

It:
- creates a TCP socket client
- connects to Laptop 2 on port `5000`
- generates simulated temperature values
- sends one value every 2 seconds

The file `edge_device.py` runs on Laptop 2.

It:
- creates a TCP socket server on port `5000`
- accepts incoming sensor data from Laptop 1
- reads each temperature value
- publishes the same value to the MQTT topic

---

## 3. MQTT Topic Used
```text
savonia/iot/temperature/adnan
```

---

## 4. Broker Used
```text
broker.emqx.io
```

Port used:
```text
1883
```

---

## 5. Files in This Repository
```text
socket_sensor.py
edge_device.py
README.md
```

---

## 6. How to Run the System

### Laptop 2 (Edge Device)
First install the MQTT library:

```bash
pip install paho-mqtt
```

Then run:

```bash
python edge_device.py
```

### Laptop 1 (Sensor)
Open `socket_sensor.py` and change this line to the IP address of Laptop 2:

```python
EDGE_DEVICE_IP = "127.0.0.1"
```

Then run:

```bash
python socket_sensor.py
```

---

## 7. Grafana Configuration
Install Grafana on **Laptop 1** and open it in the browser.

### Login
- Username: `admin`
- Password: `admin`

### Add MQTT Data Source
In Grafana:
1. Go to **Connections**
2. Click **Add new connection** or **Add new data source**
3. Search for **MQTT**
4. Select the MQTT data source
5. Configure it using:

```text
Broker: broker.emqx.io
Port: 1883
Topic: savonia/iot/temperature/adnan
```

Save the data source.

### Create Dashboard
1. Create a **new dashboard**
2. Add a **new panel**
3. Select the **MQTT** data source
4. Subscribe to this topic:

```text
savonia/iot/temperature/adnan
```

5. Choose a suitable visualization such as:
   - Time series
   - Gauge
   - Stat

---

## 8. Screenshot of the Grafana Dashboard
After running both Python programs and connecting Grafana to the MQTT topic, take a screenshot of the dashboard and paste it here before submission.

```text
[Insert your Grafana dashboard screenshot here]
```

---

## 9. Short Explanation of What Is Shown in the Panel
The Grafana panel shows the **live temperature values** coming from the sensor script on Laptop 1.
The values are first sent through a TCP socket to Laptop 2, then Laptop 2 publishes them to the MQTT broker.
Grafana subscribes to the same MQTT topic and updates the panel in real time whenever a new value arrives.

---

## 10. Short Note About the Limitation of Live-Only MQTT Visualization
This setup is mainly for **live monitoring**.
The MQTT data source in Grafana shows values that are arriving right now, but it does **not automatically store historical data** for long-term analysis.
If historical graphs are needed, the MQTT messages must also be saved into a database such as InfluxDB, PostgreSQL, or another time-series database.

---

## 11. Reflection Questions

### 1. What is the role of Grafana in this system?
Grafana is the **visual monitoring tool** in this system. It subscribes to the MQTT topic and displays the sensor data in a dashboard so that the user can observe changes in real time.

### 2. Why is MQTT useful for monitoring applications?
MQTT is useful because it is **lightweight, fast, and efficient**. It works well for IoT systems where devices send small messages frequently. It also uses a publish-subscribe model, which makes it easy for multiple clients to receive the same data stream.

### 3. What is the difference between live monitoring and historical storage?
**Live monitoring** means viewing data as it arrives right now.
**Historical storage** means saving data so it can be viewed later, analyzed over time, and used for reports or trend analysis.
In this lab, Grafana is used mainly for live monitoring, not long-term storage.

---

## 12. Learning Outcome
After completing this lab, the system demonstrates that the user can:

- forward sensor data from socket communication into MQTT
- connect Grafana to an MQTT stream
- create a simple live dashboard
- explain the role of monitoring tools in IoT systems
