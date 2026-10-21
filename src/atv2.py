import numpy as np
import streamlit as st
from PIL import Image, ImageDraw

st.title("Bandeira do Chile")

img = np.zeros((100, 150, 3), dtype=np.uint8)

# Fundo vermelho
img[:, :] = [218, 41, 28]

# Metade superior branca
img[0:50, :] = [255, 255, 255]

# Quadrado azul
img[0:50, 0:50] = [0, 57, 166]

st.image(img)
st.write("Bandeira do chile")