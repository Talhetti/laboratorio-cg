import streamlit as st
import numpy as np

st.title("Olá")
st.title("Meu nome é Alvaro")
n = st.slider("Escolha um número", 0, 100, 25)
img = np.random.randint(0, 256, (n, n), dtype=np.uint8)
st.image(img, caption=f"Imagem de {n}x{n} pixels", width=300)
st.write(img)
