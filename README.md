# Face_Detection-
Objective
The objective of this project was to design a face detection system using OpenCV and Python, which controls an LED on an ESP32 board. When a face is detected in the camera frame, the LED is turned on. When no face is detected, the LED is turned off. This system demonstrates the integration of computer vision with microcontroller-based hardware for real-time control.

System Components
Hardware:

ESP32 Board: A low-cost microcontroller with built-in Wi-Fi, used to control the LED.
LED: Connected to the ESP32 board, it serves as the output device that gets toggled on and off.
Computer with Camera: A webcam or built-in camera on a laptop used to capture the video feed for face detection.
Software:

Python: Used to run the face detection algorithm and send HTTP requests to the ESP32 to control the LED.
OpenCV: A computer vision library used to detect faces from the video feed.
ESP32 Web Server (Arduino IDE): Used to receive HTTP requests from Python and control the LED based on the face detection status.
Working Principle
Face Detection:

The system continuously captures frames from the camera.
Each frame is processed by the OpenCV face detection model (haarcascade_frontalface_default.xml).
If a face is detected, the system sends an HTTP GET request to the ESP32 to turn the LED on.
If no face is detected, another HTTP GET request is sent to turn the LED off.
ESP32 Control:

The ESP32 is connected to a Wi-Fi network and runs a web server.
The ESP32 listens for HTTP requests on specific routes: /LED=ON to turn the LED on, and /LED=OFF to turn the LED off.
Upon receiving the requests, the ESP32 controls the state of the LED (on or off) accordingly.
Communication:

Python communicates with the ESP32 over the local network using HTTP requests.
The Python script sends commands based on the face detection results in real-time.
The ESP32 responds to the commands by toggling the state of the LED.
Implementation Steps
Setup ESP32 Web Server:

Configured the ESP32 to connect to a Wi-Fi network.
Created two routes on the ESP32 server: one for turning the LED on and another for turning it off.
The LED control is done by writing to a GPIO pin on the ESP32.
Face Detection in Python:

Installed OpenCV and configured a webcam for video capture.
Loaded the pre-trained Haar Cascade classifier to detect faces.
Processed each frame from the webcam and applied face detection.
Communication between Python and ESP32:

In Python, HTTP requests (requests.get) were used to communicate with the ESP32.
When a face was detected, the Python script sent a request to turn the LED on; when no face was detected, it sent a request to turn the LED off.
Testing:

The system was tested by moving faces in and out of the camera frame to observe the LED turning on and off.
The ESP32 responded correctly to the requests, and the LED changed state based on the presence or absence of faces in the frame.

Conclusion
The project successfully demonstrated the integration of face detection with hardware control using the ESP32. By detecting faces in the video feed and sending HTTP requests to the ESP32, the LED was turned on when a face was detected and off when there was no face. This project highlights the power of combining computer vision with IoT devices for real-time interactive systems.

Challenges and Future Work
Challenges: The main challenge faced during the project was ensuring stable communication between Python and ESP32, as well as handling network delays.
Future Work: The system can be extended to perform additional actions based on face detection, such as sending alerts or controlling other hardware components.
