import streamlit as st
import pandas as pd
import os

# ==========================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================

st.set_page_config(
    page_title="Automatización de Correos",
    page_icon="📧"
)

st.title("📧 Automatización de Correos")

# ==========================
# CARGAR EXCEL
# ==========================

archivo = st.file_uploader(
    "Selecciona el archivo Excel",
    type=["xlsx"]
)

# ==========================
# MOSTRAR VISTA PREVIA
# ==========================

if archivo is not None:

    df = pd.read_excel(archivo)

    st.success("✅ Archivo cargado correctamente")

    st.subheader("📄 Vista previa")

    st.dataframe(df)

    st.metric(
        "Clientes cargados",
        len(df)
    )

# ==========================
# REPORTE DE ENVÍOS
# ==========================

if os.path.exists("reporte_envios.xlsx"):

    st.subheader("📊 Reporte de Envíos")

    reporte = pd.read_excel(
        "reporte_envios.xlsx"
    )

    st.dataframe(reporte)

    st.metric(
        "Total registros",
        len(reporte)
    )

    # Mostrar enviados y errores

    if "Estado" in reporte.columns:

        enviados = len(
            reporte[
                reporte["Estado"] == "Enviado"
            ]
        )

        errores = len(
            reporte[
                reporte["Estado"] == "Error"
            ]
        )

        st.metric(
            "Correos enviados",
            enviados
        )

        st.metric(
            "Errores",
            errores
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

else:

    st.info(
        "Aún no existe un reporte generado."
    )