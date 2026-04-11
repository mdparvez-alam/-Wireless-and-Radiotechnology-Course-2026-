# Real-Time Video Streaming System

## Overview

This project demonstrates a simple real-time home monitoring system using Flask and OpenCV. It captures live video from a webcam on the sender (Laptop A) and streams it over a local network to the viewer (Laptop B).

## Files Included:
- **app.py**: Sender program that captures video from the webcam and streams it over the local network.
- **receiver.py**: (Not provided here but would be for Laptop B) program to receive the video and display it in a browser.
  
## Instructions

### Step 1: Run the Sender Program
- On **Laptop A**, run the following command to start the stream:

```bash
python app.py