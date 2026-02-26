import streamlit as st
from PIL import Image

st.title("Esta es mi primera app en la nube")

st.header("Mi primera App :)")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("Musiquita.gif")
st.image(image,caption = "Interfaces Multimodales")

texto = st.text_input("Escribe algo" , "Este es mi texto")
st.write("El texto escrito es" , texto)

st.suheader("Ahora usemos dos columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto! :D")
