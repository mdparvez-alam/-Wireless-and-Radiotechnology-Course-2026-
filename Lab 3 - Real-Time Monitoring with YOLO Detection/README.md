# Lab 3 – Real-Time Monitoring with YOLO Detection

## Participants:
- **Sender (Laptop A):** [Your Name]
- **Viewer (Laptop B):** [Partner Name]

## Sender IP Address:
- 192.168.x.x

## System Working:
- The **sender** (Laptop A) starts a Flask server that streams video captured from the webcam.
- The **viewer** (Laptop B) runs YOLO detection on each frame from the stream and displays the results.

## Instructions to Run the System:

### On Laptop A:
1. Run the `app.py` file to start streaming the webcam feed.
   ```bash
   python app.py