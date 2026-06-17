import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Automatización de Correos",
    page_icon="📧"
)

st.title("📧 Automatización de Correos")

archivo = st.file_uploader(
    "Selecciona el archivo Excel",
    type=["xlsx"]
)

if archivo is not None:

    df = pd.read_excel(archivo)

    st.success("Archivo cargado correctamente")

    st.subheader("Vista previa")

    st.dataframe(df)

    st.metric(
        "Clientes cargados",
        len(df)
    )

# ==========================
# MOSTRAR REPORTE EXISTENTE
# ==========================

if os.path.exists("reporte_envios.xlsx"):

    reporte = pd.read_excel(
        "reporte_envios.xlsx"
    )

    st.subheader("📊 Reporte de Envíos")

    st.dataframe(reporte)

    st.write(
        f"Total registros: {len(reporte)}"
    )

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