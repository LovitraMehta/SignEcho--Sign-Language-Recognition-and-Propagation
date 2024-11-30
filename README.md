# SignEcho: Sign Language Recognition and Propagation

SignEcho is an innovative project aimed at bridging the communication gap for individuals with hearing or speech impairments. By recognizing sign language gestures and translating them into text or speech, this project promotes inclusivity and better communication in everyday interactions.

## Features

- **Sign Language Recognition**: Detects and interprets various sign language gestures using machine learning.
- **Text and Speech Output**: Converts recognized gestures into readable text or audible speech.
- **Extensible Framework**: Supports the addition of new gestures and languages.
- **Real-Time Performance**: Processes inputs quickly for a smooth user experience.

## Technologies Used

- **Programming Languages**: Python
- **Libraries and Frameworks**:
  - TensorFlow
  - OpenCV
  - Tkinter
- **Hardware**: Webcam or any video input device for gesture detection
- **Others**: Pre-trained models for gesture recognition

## Installation Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or later
- pip (Python package manager)

## Steps

### Clone the Repository

```bash
git clone https://github.com/LovitraMehta/SignEcho--Sign-Language-Recognition-and-Propagation.git
cd SignEcho--Sign-Language-Recognition-and-Propagation
```

## Usage

1. Run the `gui.py` file.
2. Use a webcam to make sign language in front of the camera.
3. The system will recognize the gesture and display the corresponding text or speech output.

## Steps to Create a Model Using User-Collected Images

### 1. Collect Images
- Capture multiple images of each alphabet you want the model to recognize using `collect_images.py` file.
- Ensure diversity in lighting, background, and angles for better model accuracy.
- Save the images in separate folders corresponding to each alphabet.

### 2. Create a Dataset
- Organize the collected images into a structured dataset by running `create_dataset.py` file.

### 3. Train the Model
- Train your model using Random Forest Classifier.
- Split your dataset into training and testing sets (e.g., 80% training, 20% testing).
- Train the model using your labeled dataset and evaluate its performance on the testing set.

### 4. Test the Model
- Validate the model's accuracy and make adjustments if necessary.
- Test the model with real-time sign language to ensure it performs as expected.

### 5. Run the GUI
- Run the `gui.py` file.

---

Feel free to contribute to this project and help make communication more inclusive for everyone!


