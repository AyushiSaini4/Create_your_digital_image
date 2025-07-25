import streamlit as st
from PIL import Image, ImageDraw

st.title("🎨 Create Your Digital Art")
st.write("This app draws a rectangle, circle, and adds a custom message.")

# Add a text input
user_text = st.text_input("Enter your message for the image:", "Hi Human!")

# Button to generate image
if st.button("Generate Image"):
    # Create image
    img = Image.new('RGB', (400, 400), color='lightblue')
    draw = ImageDraw.Draw(img)
    draw.rectangle([(50, 50), (350, 350)], outline='blue', width=5)
    draw.ellipse([(150, 150), (250, 250)], fill='yellow', outline='black')
    draw.text((120, 180), user_text, fill="black")

    # Save and display
    img.save("my_digital_art.png")
    st.image("my_digital_art.png", caption="Your Digital Art")
    st.success("✅ Image created and saved as 'my_digital_art.png'")
