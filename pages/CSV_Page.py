import streamlit as st
import pandas as pd

st.title("CSV Local - Archivos Estáticos")
st.header("Carga tu archivo CSV:")

archivo = st.file_uploader("Selecciona un archivo CSV", type=["csv"])

if archivo:
    datos = pd.read_csv(archivo)
    st.success(f"{len(datos)} registros cargados.")
    st.dataframe(datos)
else:
    st.info("Sube un archivo CSV para visualizar los datos.")