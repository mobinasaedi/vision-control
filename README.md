# VisionControl 👁️

**Real-Time Computer Vision and Vision-Based Mouse Control**

VisionControl is a Python-based computer vision project developed using OpenCV. It focuses on real-time face and eye detection through a webcam, with the goal of expanding into vision-based mouse control and interactive computer automation.

The project is being developed incrementally, starting with Haar Cascade detection and gradually introducing more advanced computer vision techniques.

## 🚀 Features

### Implemented
- Real-time webcam access using OpenCV
- Face detection using Haar Cascade
- Eye detection within detected face regions
- Grayscale image processing
- Real-time bounding box visualization
- Face and eye coordinate extraction

### Planned Features
- Real-time mouse cursor movement
- Eye-tracking-based cursor control
- Hand gesture recognition
- Interactive computer control
- Improved detection accuracy and tracking

## 🛠️ Technologies

- Python
- OpenCV
- NumPy
- Haar Cascade Classifiers

## 📁 Project Structure

```text
vision-control/
│
├── haarcascade_eye.xml
├── haarcascade_frontalface_default.xml
├── MouseTracker.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/vision-control.git
```

2. Navigate to the project directory:

```bash
cd vision-control
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the main Python file:

```bash
python main.py
```

Make sure your webcam is connected and the Haar Cascade XML files are available in the project directory.

Press `q` to exit the application.

## 📌 Development Roadmap

- [x] Webcam integration
- [x] Real-time face detection
- [x] Eye detection
- [x] Bounding box visualization
- [ ] Mouse cursor movement
- [ ] Eye-tracking-based control
- [ ] Hand gesture recognition
- [ ] Advanced tracking techniques

## 🎯 Project Goal

The main goal of VisionControl is to explore real-time computer vision and develop an interactive system that can interpret visual information and translate it into computer actions.

This project is continuously evolving as part of my learning and practical experience in Python, Computer Vision, and Artificial Intelligence.

---

**Status:** In Development
