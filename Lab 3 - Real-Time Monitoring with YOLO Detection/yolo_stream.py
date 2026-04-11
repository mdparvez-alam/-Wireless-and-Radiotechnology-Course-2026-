import cv2
from ultralytics import YOLO

STREAM_URL = "http://192.168.1.20:5000/video_feed"  # Replace with actual IP of Laptop A

# Load YOLO model
model = YOLO("yolov8n.pt")  # Replace with your YOLO model file path

# Start video stream
cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print("Error: Could not open stream.")
    exit()

print("Stream opened. Running YOLO detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Run YOLO on the frame
    results = model(frame)

    # Annotate the frame with YOLO detection results
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO Home Monitoring", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()