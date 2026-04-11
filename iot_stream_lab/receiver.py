import socket
import cv2
import numpy as np

# Receiver IP address and port
HOST = 'SENDER_IP'  # Replace with sender's IP
PORT = 5000

# Set up the socket for receiving the video stream
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Create a window to display the video
cv2.namedWindow('Receiver', cv2.WINDOW_NORMAL)

# Receive and display video
while True:
    # Receive the frame from the server
    frame = b""
    while True:
        packet = client_socket.recv(4096)
        if not packet: break
        frame += packet
        
    # Convert byte data into numpy array
    nparr = np.frombuffer(frame, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        break
    
    # Display the image
    cv2.imshow('Receiver', img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the socket and the window
client_socket.close()
cv2.destroyAllWindows()