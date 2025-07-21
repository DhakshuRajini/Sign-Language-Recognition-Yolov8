# 🧠 Sign-Language-Recognition-YOLOv8

A real-time sign language recognition system built using **YOLOv8**, **MediaPipe**, **OpenCV**, and **Flask**. This project converts hand gestures into **text and speech**, aiming to assist individuals with hearing or speech impairments.

---

## 📘 About This Project

This project is a real-time Sign Language Recognition system developed using a combination of YOLOv8, MediaPipe, OpenCV, and Flask. The main goal of the project is to provide an effective and accessible way for individuals with hearing or speech impairments to communicate with others by recognizing and translating sign language gestures into both text and speech.

The system works by capturing hand gestures either from a live webcam feed or from uploaded images. YOLOv8 is used for detecting hands, while MediaPipe provides accurate hand landmark tracking. These are processed to identify the specific sign being made. Once a gesture is recognized, it is displayed as text and also converted to speech using the `pyttsx3` library.

The project features a simple web interface using Flask, where users can interact with the system via webcam or image uploads. It serves as an innovative and socially impactful application of AI and computer vision.

---

## 🎯 Project Goals

- Build a system that can recognize hand signs in real-time using a webcam or uploaded images.
- Translate recognized gestures into text and spoken output.
- Provide an accessible tool to bridge communication gaps for the speech- and hearing-impaired.

---

## 🛠️ Tools & Technologies Used

- **YOLOv8 (Ultralytics)** – for object (hand) detection  
- **MediaPipe (Google)** – for real-time hand landmark tracking  
- **OpenCV** – for image processing and webcam access  
- **Flask** – lightweight Python web framework  
- **HTML / CSS / JavaScript** – for the web front-end  
- **pyttsx3** – for converting recognized text to speech  
- **NumPy, Pillow** – supporting libraries for array and image operations

---

## ✨ Key Features

- 🔴 Real-time sign language detection via webcam  
- 🖼️ Upload image to detect signs offline  
- 📃 Output text from recognized gestures  
- 🔊 Audio feedback using text-to-speech  
- 🌐 Clean and simple web interface

---

## 🚀 How to Run the Project Locally

1. **Install dependencies**:

```bash
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000

🧾 Project Structure
SignLanguageRecognition/
├── app.py                  # Main Flask server
├── check.py                # YOLOv8 + MediaPipe logic
├── requirements.txt        # Required Python libraries
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── uploads/            # Uploaded images
├── README.md               # Project documentation
