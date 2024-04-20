import streamlit as st
import face_recognition
import numpy as np
import os
from PIL import Image

# Initialize constants
RECOGNIZED_DIR = "recognized"
ENCODINGS_FILE = "face_encodings.npy"

#load or initialize the database of face encodings
if os.path.exists(ENCODINGS_FILE):
    face_encodings_db = np.load(ENCODINGS_FILE, allow_pickle=True).item()
else:
    face_encodings_db = {}

def save_face_encoding(image, person_name, uploaded_file):
    """Encode a face, save the encoding, and save the original image."""
    encoding = face_recognition.face_encodings(image)[0]
    face_encodings_db[person_name] = encoding
    np.save(ENCODINGS_FILE, face_encodings_db)
    
    #save the uploaded image file
    original_path = os.path.join(RECOGNIZED_DIR, f"{person_name}.{uploaded_file.name.split('.')[-1]}")
    with open(original_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

def find_match_and_show(image, uploaded_file):
    """Find a match for a face in the image and show images if matched."""
    encoding = face_recognition.face_encodings(image)[0]
    distances = face_recognition.face_distance(list(face_encodings_db.values()), encoding)
    min_distance = np.min(distances)
    match_index = np.argmin(distances)
    
    if min_distance <= 0.55:
        name = list(face_encodings_db.keys())[match_index]
        original_path = os.path.join(RECOGNIZED_DIR, f"{name}.{uploaded_file.name.split('.')[-1]}")
        original_image = Image.open(original_path)
        uploaded_image = Image.open(uploaded_file)

        #convert distance to similarity percentage
        similarity = max(0, 100 - min_distance * 100) 
        st.success(f"Match found: {name} with {similarity:.2f}% similarity")
        st.image(original_image, caption="Original Image")
        st.image(uploaded_image, caption="Uploaded Image")
    else:
        st.error("No match found.")



def main():
    st.title("Face Recognition App")

    mode = st.sidebar.selectbox("Choose Mode", ["Insert New Person", "Check If Person Exists"])

    #mode to insert a new person in the system
    if mode == "Insert New Person":
        person_name = st.text_input("Person Name")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        submit_button = st.button("Submit New Person") 
        
        if submit_button and uploaded_file is not None and person_name:
            image = face_recognition.load_image_file(uploaded_file)
            save_face_encoding(image, person_name, uploaded_file)
            st.success(f"Added {person_name} to the system.")

    #mode to check if a person exists in the system
    elif mode == "Check If Person Exists":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        check_button = st.button("Check Person")
        
        if check_button and uploaded_file is not None:
            image = face_recognition.load_image_file(uploaded_file)
            find_match_and_show(image, uploaded_file)

if __name__ == "__main__":
    main()
