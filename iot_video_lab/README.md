
# Automated Video Capture and Transfer System

## Overview
This project simulates an automated system that captures short video clips, saves them locally, and transfers them to another device over the network. Once the receiver confirms the transfer, the local copy is deleted.

## Components

1. **Sender**: Captures and sends video files to the receiver.
2. **Receiver**: Receives the video files and stores them.

## Files
- `sender.py`: The script running on the sender device, responsible for capturing and sending the videos.
- `receiver.py`: The script running on the receiver device, responsible for receiving and storing the videos.
- `videos/`: Directory where the sender saves videos before transfer.
- `received_videos/`: Directory where the receiver stores the received videos.

## How to Run

### Receiver
Run the following command on Laptop B:
```
python receiver.py
```

### Sender
Run the following command on Laptop A:
```
python sender.py
```

Make sure both laptops are connected to the same Wi-Fi network.

## Configuration
Replace `RECEIVER_IP` in `sender.py` with the actual IP address of Laptop B.

## Expected Behavior
- The sender captures a new video every 2 minutes, saves it locally, and sends it to the receiver.
- The receiver stores the received videos in `received_videos/`.
- After the receiver confirms the transfer, the sender deletes the local video file.

## Troubleshooting
- Ensure both laptops are on the same Wi-Fi network.
- Check firewall settings if there are connection issues.

