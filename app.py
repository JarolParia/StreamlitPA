import streamlit as st

st.title("Mi Aplicación de Datos")
st.sidebar.header("Configuración")
persona = st.sidebar.text_input("Escribe tu nombre", "Persona")
st.header(f"Bienvenido, {persona}!")

st.markdown("""
### Fuentes de información disponibles:
- **Base de Datos**: Registros en MongoDB Atlas
- **API Externa**: Consumo de datos en tiempo real  
- **CSV Local**: Lectura de archivos estáticos

Usa el menú lateral para navegar.
""")