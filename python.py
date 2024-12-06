import cv2
import requests

# ESP32 IP Address (change this to the actual IP address of your ESP32)
esp32_ip = "http://192.168.144.71"  # Replace with your ESP32's IP address

# Function to turn the LED on
def turn_led_on():
    url = f"{esp32_ip}/LED=ON"
    response = requests.get(url)
    if response.status_code == 200:
        print("LED turned ON")
    else:
        print("Failed to turn LED ON")

# Function to turn the LED off
def turn_led_off():
    url = f"{esp32_ip}/LED=OFF"
    response = requests.get(url)
    if response.status_code == 200:
        print("LED turned OFF")
    else:
        print("Failed to turn LED OFF")

# Load the Haar Cascade for face detection
# You may need to change the path depending on your OpenCV installation
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If faces are detected, turn the LED on, else turn it off
    if len(faces) > 0:
        print("Face detected!")
        turn_led_on()  # Turn LED on
    else:
        print("No face detected!")
        turn_led_off()  # Turn LED off

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Exit when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()