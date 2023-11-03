from PIL import Image, ImageDraw
import streamlit as st

st.set_page_config(
    page_title="Create Image",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Create Image🔎")

width = st.number_input(f'*Width in px', value=None, placeholder="Type a number...", max_value=1460)
height = st.number_input(f'*Height in px', value=None, placeholder="Type a number...", max_value=1460)

option = st.selectbox(
    '*Choose a color for the image.',
    ('White', 'Black',  'Red', 'Blue', 'Green'))

if width and height:

    desired_size = (int(width), int(height))

    create_img = Image.new('RGB', desired_size, option)

    st.image(create_img, use_column_width='never', output_format='PNG')
    st.write(f'Size: {create_img.width} x {create_img.height} px')


