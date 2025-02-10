import streamlit as st

# Set the title of the app
st.title("🎉 Our First Anniversary Celebration! 🎉")

# Add a description
st.write("Welcome to our first anniversary celebration! We are excited to share this special moment with you.")

# Add a section for partners
st.header("Our Partners")
partners = ["Partner A", "Partner B", "Partner C", "Partner D"]
selected_partner = st.selectbox("Choose a partner to learn more about:", partners)

if selected_partner:
    st.write(f"You selected: **{selected_partner}**")
    st.write(f"Details about {selected_partner}...")  # You can add more details here

# Add a section for messages
st.header("Leave a Message")
message = st.text_area("What message would you like to leave for us on our anniversary?")
if st.button("Submit Message"):
    if message:
        st.success("Thank you for your message!")
        st.write(f"You said: {message}")
    else:
        st.warning("Please enter a message before submitting.")

# Add a section for anniversary memories
st.header("Share Your Favorite Memory with Us")
memory = st.text_input("What is your favorite memory with us?")
if st.button("Share Memory"):
    if memory:
        st.success("Thank you for sharing your memory!")
        st.write(f"Your memory: {memory}")
    else:
        st.warning("Please enter a memory before sharing.")

# Add a fun image or GIF
st.header("Celebration Time!")
st.image("https://example.com/your-anniversary-image.jpg", caption="Happy Anniversary!", use_column_width=True)

# Add a footer
st.write("Thank you for being a part of our journey! Here's to many more anniversaries together! 🎊")
