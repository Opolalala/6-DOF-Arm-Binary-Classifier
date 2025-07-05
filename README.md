## 🔴🟢 Arduino-Based Color Classifier Robot

This project is a **color-based object classifier** using **TensorFlow** and **Arduino**. A neural network is trained to distinguish between **red and green cubes** using images captured on a phone. Based on the classification result, a **robotic arm** (controlled by Arduino and servos) moves accordingly to seperate them.

---

## 🧠 What It Does

1. Images of red and green cubes are collected from a local dataset.
2. A Convolutional Neural Network (CNN) is trained to classify them.
3. A new image is passed to the model.
4. Based on the prediction (`'r'` or `'g'`), the Python script sends a command to Arduino.
5. The robotic arm moves to a predefined location to seperate red or green objects.

---

## 🤖 Hardware Used

Arduino Uno or Nano

PCA9685 PWM driver

6 DOF robotic arm (servo-based)

MG996R servos

USB connection to PC

## 🧪 Example

A red cube image will send 'r' to the Arduino. The arm will:

Move to the default position

Rotate to place the red object in its designated place

For green cube, it sends 'g', triggering a different movement.

## 📸 Dataset
100+ images taken using a phone

Manually resized to (360x640)

## 📬 Future Improvements
Add blue and yellow for multi-class classification

Integrate real-time video using OpenCV or webcam

Use object detection instead of just classification

## 👩‍💻 Created By
Nujhatun Nawar — [Project powered by TensorFlow + Arduino]
