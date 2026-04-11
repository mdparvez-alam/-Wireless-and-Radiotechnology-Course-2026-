
# Lab 2 - Multi-Sensor IoT Dashboard

## System Overview
This system consists of three components:

1. **Sensor Node (Laptop 1)**: 
    - Uses socket communication to simulate temperature, humidity, and light sensor data.
    
2. **Edge Device (Laptop 2)**: 
    - Receives data from the sensor node and forwards it via MQTT to an MQTT Broker.
    
3. **MQTT Broker**: 
    - Acts as a central communication hub to handle MQTT messages.
    
4. **Grafana Dashboard (Laptop 1)**: 
    - Displays real-time data from the sensors on a 4-panel monitoring dashboard.

## Sensor Nodes
- **Temperature Sensor**: Random temperature readings between 20 and 35°C.
- **Humidity Sensor**: Random humidity readings between 40 and 80%.
- **Light Sensor**: Random light intensity readings between 100 and 1000 lux.

## MQTT Topics Used
- **savonia/iot/temperature**: For temperature readings.
- **savonia/iot/humidity**: For humidity readings.
- **savonia/iot/light**: For light intensity readings.

## Grafana Dashboard Layout
The dashboard consists of four panels:
1. **Temperature Graph**: A graph displaying temperature changes over time.
2. **Humidity Gauge**: A gauge displaying the current humidity percentage.
3. **Light Gauge**: A gauge displaying the current light intensity (in lux).
4. **Status Panel**: Displays the status of the sensors (temperature, humidity, light).

### Screenshot of the 4-panel dashboard (add after running Grafana)

## Explanation of Dashboard Layout
The dashboard provides real-time monitoring of three sensor values (temperature, humidity, light) and their corresponding gauges.

## Reflection Question
### Why do we separate each sensor into a different MQTT topic?
Each sensor is separated into a different MQTT topic to allow independent tracking, monitoring, and processing of data streams. This separation also provides flexibility in scaling and managing sensor data.

