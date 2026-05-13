import streamlit as st 

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por Gianella Z.")

Sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"])

if sesion == "Sesión 1":
    st.write("Bienvenido a la sesión 1")
  st.image ("Image20260512194059.png)

elif  sesion == "Sesión 2":
    st.write("Bienvenido a la sesión 2")

else:
  st.write("Bienvenido a la sesión 4")
