
---

## Description
This application utilizes the face_recognition library to perform face detection and recognition tasks. It provides a simple Streamlit interface where users can either insert a new person into the system or check if a person exists based on their facial features. The application leverages the "Labeled Faces in the Wild" (LFW) dataset, which provides a variety of images with multiple pictures per person, to enhance the accuracy and reliability of the face recognition process.

## Features
- **Insert New Person:** Add a person's name and their face encoding to the database.
- **Check If Person Exists:** Check an uploaded image against the database to see if the person is already recognized.

## Live Access

This application can also be viewed online at the following URL: [CNN Face Recognition App](https://cnn-face-recognition-app.streamlit.app).


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nikhildhoka8/Biometrics-Final-Project.git
   ```

2. **Install the required packages:**
   ```bash
   pip install streamlit face_recognition numpy pillow
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage
- Launch the app and select a mode from the sidebar.
- **Insert New Person:** Enter the name and upload an image. Press "Submit New Person".
- **Check If Person Exists:** Upload an image and press "Check Person".

## Sources and Acknowledgements
- **face_recognition:** Developed by Adam Geitgey, this library provides powerful and efficient tools for facial recognition tasks. [GitHub link](https://github.com/ageitgey/face_recognition)
- **NumPy:** Used for handling large, multi-dimensional arrays and matrices. [Official site](https://numpy.org/)
- **PIL (Pillow):** A Python Imaging Library that adds support for opening, manipulating, and saving many different image file formats. [PyPI link](https://pypi.org/project/Pillow/)
- **Streamlit:** An open-source app framework for Machine Learning and Data Science projects. [Official site](https://streamlit.io/)
- **LFW Dataset:** Used to retrieve images for face recognition training and testing. The dataset contains more than 13,000 images of faces collected from the web. [LFW Dataset](http://vis-www.cs.umass.edu/lfw/)

---