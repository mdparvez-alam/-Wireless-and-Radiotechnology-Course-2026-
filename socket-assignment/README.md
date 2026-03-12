# Socket Programming with Python

## Project Description
This project is a simple TCP client-server communication system written in Python.  
The server waits for a client connection and receives sensor-like temperature data.  
The client connects to the server and sends random temperature values every 5 seconds.

## Files
- `server.py` → Receives and displays incoming messages from the client
- `client.py` → Generates random temperature data and sends it to the server
- `README.md` → Project explanation and test results

## Requirements
- Python 3.x

## How to Run

### 1. Run the server
```bash
python server.py