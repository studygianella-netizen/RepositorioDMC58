import streamlit as st 

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por Gianella Z.")

Sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"])

if Sesion == "Sesión 1":
    st.write("Bienvenido la sesión 1")
    
elif  Sesion == "Sesión 2":
    st.write("Bienvenido la sesión 2")
    
elif  Sesion == "Sesión 3":
    st.write("Bienvenido la sesión 3")
    
else
    st.write("Bienvenido la sesión 4")
