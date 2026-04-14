import streamlit as st
from conexion import conectionBd

def main():
    db = conectionBd("StreamAPP")
    st.title("Hello, Streamlit!")
    st.sidebar.header("configuracion")
    persona = st.sidebar.text_input("Ingresa tu nombre","Persona")
    st.title(f'Hola {persona}!')
    st.header("Mis datos:")
    usuarios = list(db["usuarios"].find({},{"_id":0}))

    if usuarios:
        st.dataframe(usuarios)
    else:
        st.write("No hay usuarios registrados.")
        



if __name__ == "__main__":
    main()
