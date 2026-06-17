import streamlit as st
import pandas as pd
import os

# ==========================
# CONFIGURACIÓN
# ==========================

st.set_page_config(
    page_title="Automatización de Correos",
    page_icon="📧"
)

st.title("📧 Automatización de Correos")

# ==========================
# SUBIR ARCHIVO
# ==========================

archivo = st.file_uploader(
    "Selecciona el archivo Excel",
    type=["xlsx"]
)

# ==========================
# SI NO HAY ARCHIVO
# ==========================

if archivo is None:
    st.info("📂 Carga un archivo Excel para comenzar")

# ==========================
# SI HAY ARCHIVO
# ==========================

if archivo is not None:

    # Leer Excel
    df = pd.read_excel(archivo)

    st.success("✅ Archivo cargado correctamente")

    # Vista previa
    st.subheader("📄 Vista previa")

    st.dataframe(df)

    # Cantidad de clientes
    st.metric(
        "Clientes cargados",
        len(df)
    )

    # Mostrar reporte si existe
    if os.path.exists("reporte_envios.xlsx"):

        reporte = pd.read_excel(
            "reporte_envios.xlsx"
        )

        st.subheader("📊 Reporte de Envíos")

        st.dataframe(reporte)

        st.metric(
            "Total registros",
            len(reporte)
        )

        # Descargar reporte
        with open(
            "reporte_envios.xlsx",
            "rb"
        ) as archivo_reporte:

            st.download_button(
                label="📥 Descargar Reporte",
                data=archivo_reporte.read(),
                file_name="reporte_envios.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )