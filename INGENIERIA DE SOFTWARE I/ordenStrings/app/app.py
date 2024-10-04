import streamlit as st
from string import cargar_cadenas_desde_archivo, guardar_cadenas_en_archivo, ordenar_cadenas
from number import cargar_numeros_desde_archivo, guardar_numeros_en_archivo, ordenar_numeros

def main():
    st.set_page_config(page_title="Ordenador de Cadenas y Números", layout="centered")
    st.title("📑 Ordenador de Cadenas y Números")
    
    # Barra lateral
    st.sidebar.title("Información")
    st.sidebar.markdown("""
    Esta aplicación web te permite ordenar **cadenas** o **números** de forma ascendente o descendente.
    
    **Opciones:**
    - Ordenar cadenas.
    - Ordenar números.
    
    **Desarrollado con:** Streamlit
    """)
    
    # Selección de opción
    opcion = st.selectbox("Selecciona el tipo de datos a ordenar:", ("Cadenas", "Números"))
    
    if opcion == "Cadenas":
        st.header("Ordenar Cadenas")
        archivo_subido = st.file_uploader("Carga un archivo de texto con las cadenas a ordenar", type=["txt"])
        
        if archivo_subido:
            cadenas = [line.decode('utf-8').strip() for line in archivo_subido.readlines()]
            st.write("Cadenas cargadas:")
            st.write(cadenas)
            
            orden = st.radio("Selecciona el orden:", ("Ascendente", "Descendente"))
            ascendente = True if orden == "Ascendente" else False
            cadenas_ordenadas = ordenar_cadenas(cadenas, ascendente=ascendente)
            
            st.write("Cadenas ordenadas:")
            st.write(cadenas_ordenadas)
            
            if st.button("Guardar cadenas ordenadas en un archivo"):
                ruta_archivo_salida = st.text_input("Ingresa el nombre del archivo para guardar:", "cadenas_ordenadas.txt")
                guardar_cadenas_en_archivo(cadenas_ordenadas, ruta_archivo_salida)
                st.success(f"Cadenas guardadas en '{ruta_archivo_salida}'.")
    
    elif opcion == "Números":
        st.header("Ordenar Números")
        archivo_subido = st.file_uploader("Carga un archivo de texto con los números a ordenar", type=["txt"])
        
        if archivo_subido:
            contenido = archivo_subido.read().decode('utf-8')
            lineas = contenido.strip().split('\n')
            numeros = []
            for linea in lineas:
                try:
                    numero = float(linea.strip())
                    numeros.append(numero)
                except ValueError:
                    st.warning(f"'{linea.strip()}' no es un número válido y será ignorado.")
            
            st.write("Números cargados:")
            st.write(numeros)
            
            orden = st.radio("Selecciona el orden:", ("Ascendente", "Descendente"))
            ascendente = True if orden == "Ascendente" else False
            numeros_ordenados = ordenar_numeros(numeros, ascendente=ascendente)
            
            st.write("Números ordenados:")
            st.write(numeros_ordenados)
            
            if st.button("Guardar números ordenados en un archivo"):
                ruta_archivo_salida = st.text_input("Ingresa el nombre del archivo para guardar:", "numeros_ordenados.txt")
                guardar_numeros_en_archivo(numeros_ordenados, ruta_archivo_salida)
                st.success(f"Números guardados en '{ruta_archivo_salida}'.")
    
    st.markdown("""
    <style>
    .css-1d391kg {text-align: center;}
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
