import streamlit as st
import io

def main():
    # Configuración de la página
    st.set_page_config(page_title="Ordenador de Datos", page_icon="📊", layout="centered")
    st.title("📋 Ordenador de Cadenas y Números")
    st.markdown("---")

    # Barra lateral con descripción y opciones
    st.sidebar.title("Opciones")
    st.sidebar.write("Esta aplicación te permite ordenar **cadenas** o **números** en orden ascendente o descendente. Puedes cargar los datos desde un archivo, visualizarlos, ordenarlos y guardar el resultado en otro archivo.")

    # Selección del tipo de datos
    data_type = st.sidebar.selectbox("Selecciona el tipo de datos", ["Cadenas", "Números"])

    # Selección del orden
    sort_order = st.sidebar.radio("Selecciona el orden", ["Ascendente", "Descendente"])

    # Carga de archivo
    st.header("Carga de Archivo")
    uploaded_file = st.file_uploader("Selecciona un archivo de texto", type=["txt", "csv"])

    if uploaded_file is not None:
        try:
            # Lectura y procesamiento del archivo
            content = uploaded_file.read().decode('utf-8')
            data = content.strip().splitlines()
            if data_type == "Números":
                data = [float(item.strip()) for item in data if item.strip()]
            else:
                data = [item.strip() for item in data if item.strip()]

            # Visualización del contenido original
            st.subheader("Contenido del Archivo")
            st.write(data)

            # Ordenamiento de los datos
            reverse_order = True if sort_order == "Descendente" else False
            sorted_data = sorted(data, reverse=reverse_order)

            # Visualización de los datos ordenados
            st.subheader(f"Datos Ordenados ({sort_order})")
            st.write(sorted_data)

            # Preparación de los datos para descarga
            if data_type == "Números":
                output_data = '\n'.join([str(item) for item in sorted_data])
            else:
                output_data = '\n'.join(sorted_data)
            output = io.BytesIO()
            output.write(output_data.encode('utf-8'))
            output.seek(0)

            # Botón de descarga
            st.download_button(
                label="💾 Descargar Datos Ordenados",
                data=output,
                file_name='datos_ordenados.txt',
                mime='text/plain'
            )

        except Exception as e:
            st.error(f"Error al procesar el archivo: {e}")
    else:
        st.info("Por favor, carga un archivo para continuar.")

if __name__ == "__main__":
    main()
