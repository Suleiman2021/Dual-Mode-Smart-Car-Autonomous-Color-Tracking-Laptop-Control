##Dual-Mode Smart Car — Autonomous Color Tracking & Laptop Control

This project implements a dual-mode smart robotic vehicle powered by an ESP32 and controlled via Python, OpenCV, and a Kivy UI interface.
The system can operate autonomously by tracking colors using a smartphone camera, or manually through a laptop control interface.

🎯 Project Goals

Create a robotic car capable of color-based autonomous navigation

Provide a manual driving mode using buttons on a laptop

Send simple single-character commands to the ESP32 for movement

Combine computer vision, socket communication, and embedded motor control

🚗 How the System Works
1️⃣ Autonomous Color-Tracking Mode

A smartphone camera is mounted at the front of the car.
The camera feed is sent to the Python script (main.py), which uses OpenCV to:

Convert each frame to HSV

Apply color masks (yellow, green, red, blue)

Detect large contours

Determine which color is visible

Send a corresponding movement command to the ESP32

Color → Movement Mapping
Color	Command	Action
Yellow	'U'	Move Forward
Green	'L'	Turn Left
Red	'B'	Move Backward
Blue	'R'	Turn Right

The ESP32 receives these commands over Wi-Fi (TCP socket) and controls the motors accordingly.

2️⃣ Manual Laptop Control Mode

A Kivy interface (control.kv) provides on-screen buttons such as:

Front

Back

Left

Right

Stop

When the user clicks a button, main.py sends the matching character:

Button	Command
Front	'u'
Back	'b'
Left	'l'
Right	'r'
Stop	's'

The ESP32 interprets these characters and drives the motors.

🧠 System Architecture
Smartphone Camera → Python (OpenCV) → Wi-Fi Socket → ESP32 → Motor Driver → Car Motion
Laptop Buttons  → Python (Kivy UI) → Wi-Fi Socket → ESP32 → Motor Driver → Car Motion

📂 Repository Structure
/
├── main.py          # Color tracking + socket commands + Kivy logic
├── control.kv       # UI layout for manual driving
├── SUPER_CAR.ino    # ESP32 firmware controlling motors
├── README.md        # Project documentation
└── demo_video.mp4   # (Optional) demonstration video

🛠 Technologies Used
Software

Python

OpenCV

Kivy

imutils

ESP32 Arduino Framework

TCP Socket Networking

Hardware

ESP32 Wi-Fi module

Smartphone camera

Motor driver (L298N or similar)

DC motors

Car chassis + battery

🔌 Communication Protocol

The Python app sends a single character to the ESP32 server at:

IP:   192.168.4.1
Port: 80


Example:

sock = socket.socket()
sock.connect((host, port))
sock.send(b'U')   # Move forward
sock.close()

🚀 How to Run the Project
1. Flash ESP32

Upload SUPER_CAR.ino to the ESP32.
The ESP32 becomes a Wi-Fi Access Point and starts a server at port 80.

2. Connect the Laptop to ESP32 Wi-Fi

Example SSID:

ESP32-Car

3. Start Python Program
python main.py

4. Choose Mode

Manual Mode: Use UI buttons

Autonomous Mode: Enable tracking and show a color in front of the camera



📌 Future Improvements

Add PID steering

Improve color detection robustness

Add Bluetooth/HTTP/WebSocket control

Add voice-control mode

Add obstacle avoidance
