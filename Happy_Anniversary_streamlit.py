import streamlit as st
from PIL import Image
import os

# Create a directory to store uploaded files
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Set the title of the app
st.title("💖 Our Memories Together 💖")

# Add a description
st.write("Welcome to our memory lane! Here, we celebrate our moments, messages, and music.")

# Section for uploading images
st.header("Upload Your Favorite Images")
uploaded_files = st.file_uploader("Choose images to upload", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save the uploaded file to the uploads directory
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name, use_column_width=True)

# Section for sharing moments
st.header("Share a Special Moment")
moment = st.text_area("What is a special moment you'd like to share?")
if st.button("Submit Moment"):
    if moment:
        st.success("Thank you for sharing your moment!")
        st.write(f"You shared: {moment}")
    else:
        st.warning("Please enter a moment before submitting.")

# Section for messages
st.header("Leave a Message")
message = st.text_area("What message would you like to leave for us?")
if st.button("Submit Message"):
    if message:
        st.success("Thank you for your message!")
        st.write(f"You said: {message}")
    else:
        st.warning("Please enter a message before submitting.")

# Section for uploading a cover song
st.header("Upload Your Cover Song")
uploaded_song = st.file_uploader("Choose an audio file to upload", type=["mp3", "wav"])

if uploaded_song:
    # Save the uploaded song to the uploads directory
    with open(os.path.join("uploads", uploaded_song.name), "wb") as f:
        f.write(uploaded_song.getbuffer())
    st.audio(uploaded_song, format='audio/mp3')

# Add a footer
st.write("Thank you for being a part of our journey! Here's to many more memories together! 🎊")
