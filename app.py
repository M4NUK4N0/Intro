import streamlit as st
from PIL import Image

st.title("Esta es mi primera app en la nube")

st.header("Mi primera App :)")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("Musiquita.GIF")
st.image(image,caption = "Interfaces Multimodales")
