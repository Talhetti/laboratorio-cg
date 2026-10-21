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

# Estrela branca de cinco pontas
centro_x, centro_y = 25, 25
raio_externo, raio_interno = 18, 7
angulos = np.linspace(-np.pi / 2, 3 * np.pi / 2, 10, endpoint=False)
raios = np.tile([raio_externo, raio_interno], 5)
pontos = [
    (
        centro_x + raio * np.cos(angulo),
        centro_y + raio * np.sin(angulo),
    )
    for angulo, raio in zip(angulos, raios)
]

imagem = Image.fromarray(img)
ImageDraw.Draw(imagem).polygon(pontos, fill=(255, 255, 255))

st.image(imagem)
