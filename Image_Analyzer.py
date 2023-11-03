from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Image Analyzer",
    page_icon="🔎"
)

st.title("Image Analyzer 🔎")

MM_CONVERSION = 0.2645833333
IN_CONVERSION = 0.0104166667

uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg'])

if uploaded_file is not None:
    with Image.open(uploaded_file) as img:
        st.image(img, use_column_width='auto')

    st.write(f'Format: {img.format}')
    st.write(f'Size px: {img.width} x {img.height} px')
    st.write(f'Has Transparency Data: {img.has_transparency_data}')
    st.write(f'Mode: {img.mode}')
    st.write(f'Exif data: {img.getexif()}')
    if img.info:
        try:
            st.write(f'Dpi: {img.info["dpi"][0]:.1f}')

            width_in = img.width / int(img.info["dpi"][0])
            height_in = img.height / int(img.info["dpi"][0])
            st.write(f'Size in: {width_in:.1f} x {height_in:.1f} in')
            st.write(f'Size mm: {width_in * 25.4:.1f} x {height_in * 25.4:.1f} mm')
        except:
            st.write(f'Information: {img.info}')