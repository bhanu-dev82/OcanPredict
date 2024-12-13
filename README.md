# OSMF Detection System

A modern web application for Oral Submucous Fibrosis (OSMF) detection using deep learning and computer vision.

## Features

- Real-time webcam capture
- Image upload capability 
- OSMF detection and classification
- Confidence score prediction
- Modern responsive UI
- Docker support

## Tech Stack

- Flask (Backend)
- HTML/CSS/JavaScript (Frontend)
- YOLO (Deep Learning Model)
- OpenCV (Image Processing)
- Docker (Containerization)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/osmf-detection.git
cd osmf-detection

README.md
Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Docker Deployment
Build the Docker image:
docker build -t osmf-detection .

Run the container:
docker run -p 5000:5000 osmf-detection

Project Structure
osmf-detection/
├── app.py
├── requirements.txt
├── Dockerfile
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── models/
    └── best.pt

Usage
Open your browser and navigate to http://localhost:5000
Choose between:
Uploading an image
Capturing through webcam
Click "Analyze" to get OSMF detection results
Model Information
The system uses a YOLO-based model trained on OSMF images for:

Classification
Confidence scoring
Real-time detection
