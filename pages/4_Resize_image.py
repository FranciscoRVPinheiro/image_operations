from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Resize Image",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Resize Image 🔎")

uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg'])

if uploaded_file is not None:
    with Image.open(uploaded_file) as img:
        st.write(f'Size px: {img.width} x {img.height} px')
        st.image(img)

        width = st.number_input(f'*New width in px', value=None, placeholder="Type a number...", max_value=1460)
        height = st.number_input(f'*New height in px', value=None, placeholder="Type a number...", max_value=1460) 

        if width and height:
            resized = img.resize((int(width), int(height)))
            st.image(resized)

    