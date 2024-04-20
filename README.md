
---

## Description
This application utilizes the face_recognition library to perform face detection and recognition tasks. It provides a simple Streamlit interface where users can either insert a new person into the system or check if a person exists based on their facial features.

## Features
- **Insert New Person:** Add a person's name and their face encoding to the database.
- **Check If Person Exists:** Check an uploaded image against the database to see if the person is already recognized.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
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
- **Streamlit:** An open-source app framework for Machine Learning and Data Science projects. [Official site](https://streamlit.io/).

---

### Note:
Make sure to replace `<repository-url>` with the actual URL of your Git repository where this code will be hosted. This README.md file is designed to be placed in the root of your project directory. Ensure that all software dependencies are appropriately credited and that usage instructions are clear for end users.