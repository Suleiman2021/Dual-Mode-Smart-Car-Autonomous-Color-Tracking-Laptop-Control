تمام! سأعطيك **README منسق باحترافية عالية** وبعناوين كبيرة وواضحة مثل مشاريع GitHub الكبيرة.
هذا التنسيق ممتاز، نظيف، ويبدو جميلًا جدًا داخل GitHub.

---

# 📘 **Dual-Mode Smart Car — Autonomous Color Tracking & Laptop Control**

This project implements a smart robotic vehicle controlled by **Python**, **OpenCV**, **Kivy**, and an **ESP32**.
The car can operate in two modes:

* **Autonomous Color Tracking** (moves based on detected color)
* **Manual Laptop Control** (buttons send commands to ESP32)

---

# 🚗 Overview

A smartphone camera placed at the front of the car sends live video to `main.py`.
The Python script detects colors and sends **single-character commands** to the ESP32 via Wi-Fi.
The ESP32 receives the commands and controls the motors.

In manual mode, the user presses buttons in the Kivy interface, and each button sends a command to the ESP32.

---

# 🔥 Features

* Autonomous navigation using **color detection**
* Manual navigation using **Kivy UI**
* Real-time camera processing
* Wi-Fi socket communication with ESP32
* Simple command protocol (single-character commands)
* Fast & lightweight control method

---

# 🧠 How the System Works

## **1️⃣ Autonomous Color Tracking Mode**

Python + OpenCV:

* Converts frame → HSV
* Detects colors (yellow, green, red, blue)
* Identifies contours
* Sends movement command based on detected color

### **Color → Action Mapping**

| Color  | Command | Action        |
| ------ | ------- | ------------- |
| Yellow | `U`     | Move Forward  |
| Green  | `L`     | Turn Left     |
| Red    | `B`     | Move Backward |
| Blue   | `R`     | Turn Right    |

---

## **2️⃣ Manual Laptop Control Mode**

The Kivy UI (`control.kv`) provides buttons:

* **Front**
* **Back**
* **Left**
* **Right**
* **Stop**

Each button sends a lowercase command:

| Button | Command |
| ------ | ------- |
| Front  | `u`     |
| Back   | `b`     |
| Left   | `l`     |
| Right  | `r`     |
| Stop   | `s`     |

---

# 🔌 Communication Protocol

The Python app connects to the ESP32 Wi-Fi server at:

```
Host: 192.168.4.1
Port: 80
```

and sends one character per command.

---

# 🛠 Technologies Used

### **Software**

* Python
* OpenCV
* Kivy
* imutils
* ESP32 Arduino Framework
* TCP Sockets

### **Hardware**

* ESP32
* Motor Driver (L298N)
* DC Motors
* Smartphone camera
* Car chassis

---

# 📂 Repository Structure

```
/
├── main.py          # Python: color tracking + socket control + Kivy UI logic
├── control.kv       # Kivy interface (layout)
├── SUPER_CAR.ino    # ESP32 firmware (motor controller)
├── README.md        # Project documentation
└── demo.mp4         # (optional) demonstration video
```

---

# 🚀 How to Run

## **1. Flash the ESP32**

Upload `SUPER_CAR.ino`.

## **2. Connect Laptop to ESP32 Wi-Fi AP**

Example SSID:

```
ESP32-Car
```

## **3. Run Python Program**

```bash
python main.py
```

## **4. Select Mode**

* Manual → use buttons
* Autonomous → show the target color to the camera

---

# 🎥 Demo

(Add your video here)

---

# 🧩 Future Improvements

* Add PID steering
* Add obstacle avoidance
* Improve color detection filters
* Add mobile app control

---

إذا تريد، أستطيع أن:

✅ أضيف أيقونات جميلة
✅ أضيف صور داخل الـ README
✅ أضيف GIF للحركة
✅ أصنع لك **Badge Icons** مثل:

`![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-blue)`

هل تريد نسخة أكثر جمالًا مع أيقونات وعناصر إضافية؟
