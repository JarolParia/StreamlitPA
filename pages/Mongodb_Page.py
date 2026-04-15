import streamlit as st
import pandas as pd
from conexion import conectionBd

st.title("Base de datos - MongoDB")
st.header("Registros en BD:")

db = conectionBd("StreamAPP")
usuarios = list(db["usuarios"].find({},{"_id":0}))

if usuarios:
    st.dataframe(pd.DataFrame(usuarios))
else:
    st.warning("No hay registros de usuarios en la base de datos")
