from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Rotate Image",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Rotate Image🔎")

uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg'])

if uploaded_file is not None:
    with Image.open(uploaded_file) as img:
        st.image(img, use_column_width='auto')

    rotation_angle = st.number_input(f'Degrees to rotate counter-clockwise', value=None, placeholder="Type a number...")

    if rotation_angle:

        rotation_angle = int(rotation_angle)

        rotated_image = img.rotate(rotation_angle, expand=True)

        st.image(rotated_image)