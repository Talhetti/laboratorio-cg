import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Padrão")

k = st.slider("k", 1, 256, 4)
y, x = np.indices((64, 64))

def padrao(x, y, k):
    return (y + 5 + ((x**2) + 32) + k) % 256

def padrao2(x, y, k):
    return (y + 2 +((x**2) + 99) + k) % 256

imagem = padrao(x, y, k).astype(np.uint8)
imagem2 = padrao2(x, y, k).astype(np.uint8)

st.image(ampliar(imagem, 4))
st.image(ampliar(imagem2, 4))