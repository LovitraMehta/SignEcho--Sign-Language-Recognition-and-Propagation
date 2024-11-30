SignEcho: Sign Language Recognition and Propagation

SignEcho is an innovative project aimed at bridging the communication gap for individuals with hearing or speech impairments. By recognizing sign language gestures and translating them into text or speech, this project promotes inclusivity and better communication in everyday interactions.

Features

Sign Language Recognition: Detects and interprets various sign language gestures using machine learning.
Text and Speech Output: Converts recognized gestures into readable text or audible speech.
User-Friendly Interface: Designed for accessibility and ease of use.
Extensible Framework: Supports the addition of new gestures and languages.
Real-Time Performance: Processes inputs quickly for smooth user experience.

Technologies Used

Programming Languages: Python, JavaScript
Libraries and Frameworks: TensorFlow, OpenCV, Flask, React.js
Hardware: Webcam or any video input device for gesture detection
Others: Pre-trained models for gesture recognition

Installation Prerequisites

Ensure you have the following installed on your system:
Python 3.7 or later
Node.js and npm
pip (Python package manager)

Steps

Clone the repository:

git clone https://github.com/LovitraMehta/SignEcho--Sign-Language-Recognition-and-Propagation.git
cd SignEcho--Sign-Language-Recognition-and-Propagation

Install Python dependencies:

pip install -r requirements.txt

Install frontend dependencies:

cd frontend
npm install

Run the application:

Start the backend server:

python app.py

Start the frontend:

cd frontend
npm start

Usage

Open the application in your web browser (usually at http://localhost:3000).
Use a webcam to make gestures in front of the camera.
The system will recognize the gesture and display the corresponding text or speech output.

Project Structure

SignEcho/
│
├── backend/              # Backend server code (Flask API)
│   ├── app.py            # Main server file
│   ├── models/           # Pre-trained gesture recognition models
│   └── ...
│
├── frontend/             # Frontend code (React.js)
│   ├── src/              # Source files for UI
│   └── ...
│
├── datasets/             # Datasets for training and testing models
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── ...
