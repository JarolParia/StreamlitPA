import streamlit as st
import pandas as pd
from clase_api import ClaseAPI

st.title("API EXTERNA - Datos en tiempo real")
st.header("Datos de la API:")

@st.cache_data
def cargar_datos_api(limite):
    cliente = ClaseAPI()
    return cliente.consultar(limite)

cantidad = st.slider("Cantidad de registros a mostrar", 1, 100, 5)
daticos = cargar_datos_api(cantidad)

if daticos:
    st.dataframe(daticos)
else:
    st.error("Error al obtener datos desde la API")

