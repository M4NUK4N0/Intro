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

st.subheader("Ahora usemos dos columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto! :D")

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que Modalidad es la principal en tu interfaz" , ("Visual","Auditiva","Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de Botones")
if st.button("Presiona el botón"):
  st.write("Gracias por presionar")
else:
  st.write("No has presionado aún")
  
