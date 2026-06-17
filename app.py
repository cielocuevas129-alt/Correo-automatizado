import streamlit as st
import pandas as pd
import os
import subprocess

# ==========================
# CONFIGURACIÓN
# ==========================

st.set_page_config(
    page_title="Automatización de Correos",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Sistema de Automatización de Correos")

st.write(
    "Carga un archivo Excel para procesar correos y generar reportes."
)

# ==========================
# CARGAR EXCEL
# ==========================

archivo = st.file_uploader(
    "Selecciona el archivo Excel",
    type=["xlsx"]
)

if archivo is None:

    st.info(
        "📂 Carga un archivo Excel para comenzar."
    )

else:

    # Guardar Excel cargado
    with open("clientes.xlsx", "wb") as f:
        f.write(archivo.getbuffer())

    df = pd.read_excel("clientes.xlsx")

    st.success(
        "✅ Archivo cargado correctamente"
    )

    st.subheader(
        "📄 Vista previa"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Clientes cargados",
            len(df)
        )

    with col2:
        st.metric(
            "Columnas",
            len(df.columns)
        )

    # ==========================
    # BOTÓN
    # ==========================

    if st.button(
        "📧 Enviar Correos",
        use_container_width=True
    ):

        st.info(
            "⏳ Procesando correos..."
        )

        # Ejecutar script principal
        subprocess.run(
            ["python", "correo_automatico.py"]
        )

        st.success(
            "✅ Proceso finalizado"
        )

        # ==========================
        # MOSTRAR REPORTE
        # ==========================

        if os.path.exists(
            "reporte_envios.xlsx"
        ):

            reporte = pd.read_excel(
                "reporte_envios.xlsx"
            )

            st.subheader(
                "📊 Reporte de Envíos"
            )

            st.dataframe(
                reporte,
                use_container_width=True
            )

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

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Enviados",
                        enviados
                    )

                with col2:
                    st.metric(
                        "Errores",
                        errores
                    )

            with open(
                "reporte_envios.xlsx",
                "rb"
            ) as archivo_reporte:

                st.download_button(
                    label="📥 Descargar Reporte",
                    data=archivo_reporte.read(),
                    file_name="reporte_envios.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )