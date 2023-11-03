from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Flip Image",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Flip Image 🔎")

uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg'])

if uploaded_file is not None:
    with Image.open(uploaded_file) as img:
        st.image(img, use_column_width='auto')

    option = st.selectbox(
    '*Choose a direction to flip.',
    ('None', 'Horizontal', 'Vertical'))
    
    if option == 'Horizontal':
        flip_horizontal = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        st.image(flip_horizontal)
    
    if option == 'Vertical':
        flip_vertical = img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
        st.image(flip_vertical)

