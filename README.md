# smart-traffic-system
A real-time traffic signal simulation and red-light violation detection system built using Python, OpenCV, and Background Subtraction
# 🚦 Smart Traffic Violation Detection System

A computer vision-based traffic management and red-light violation detection system built using Python and OpenCV. The system simulates dynamic traffic signals and detects vehicles crossing a defined stop line during a Red signal.

---

## ✨ Features

* **🚥 Traffic Light Simulation:** Automatically toggles traffic signals (GREEN / RED) at set time intervals.
* **🎥 Real-Time Motion Detection:** Uses OpenCV's `BackgroundSubtractorMOG2` to track moving objects/vehicles.
* **🛑 Stop-Line Violation Detection:** Identifies when a vehicle crosses the virtual stop line while the signal is RED.
* **📸 Automatic Snapshot Capture:** Automatically captures and saves an image proof (`violation_<timestamp>.jpg`) whenever a violation occurs.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** OpenCV (`cv2`), NumPy, Time

---

## 📂 Project Structure

```text
traffic-violation-detection/
├── traffic.py
├── README.md
└── requirements.txt
