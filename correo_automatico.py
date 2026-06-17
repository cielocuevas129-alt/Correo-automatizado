import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from reportlab.pdfgen import canvas

# ==========================
# CONFIGURACION
# ==========================

correo_emisor = "TU_CORREO@gmail.com"
password = "TU_CONTRASENA_APP"

# ==========================
# LEER EXCEL
# ==========================

df = pd.read_excel("clientes.xlsx")

registro_envios = []

# ==========================
# RECORRER CLIENTES
# ==========================

for _, fila in df.iterrows():

    correo_destino = fila["Correo"]

    nombre_excel = f"Reporte_{fila['Nombre']}.xlsx"
    nombre_pdf = f"Reporte_{fila['Nombre']}.pdf"

    # ==========================
    # CREAR EXCEL
    # ==========================

    reporte_cliente = pd.DataFrame({
        "Cliente": [fila["Nombre"]],
        "Producto": [fila["Producto"]],
        "Fecha": [datetime.now()]
    })

    reporte_cliente.to_excel(
        nombre_excel,
        index=False
    )

    # ==========================
    # CREAR PDF
    # ==========================

    pdf = canvas.Canvas(nombre_pdf)

    pdf.setTitle("Reporte Cliente")

    pdf.drawString(
        100,
        750,
        f"Cliente: {fila['Nombre']}"
    )

    pdf.drawString(
        100,
        720,
        f"Producto: {fila['Producto']}"
    )

    pdf.drawString(
        100,
        690,
        f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    )

    pdf.save()

    # ==========================
    # CREAR CORREO
    # ==========================

    mensaje = MIMEMultipart()

    mensaje["From"] = correo_emisor
    mensaje["To"] = correo_destino
    mensaje["Subject"] = "Información de Producto"

    cuerpo = f"""
Hola {fila['Nombre']},

Le informamos que su producto asignado es:

{fila['Producto']}

Adjuntamos su reporte en Excel y PDF.

Gracias por su atención.

Saludos cordiales.
"""

    mensaje.attach(
        MIMEText(cuerpo, "plain")
    )

    # ==========================
    # ADJUNTAR EXCEL
    # ==========================

    with open(nombre_excel, "rb") as adjunto_excel:

        parte_excel = MIMEBase(
            "application",
            "octet-stream"
        )

        parte_excel.set_payload(
            adjunto_excel.read()
        )

    encoders.encode_base64(parte_excel)

    parte_excel.add_header(
        "Content-Disposition",
        f"attachment; filename={nombre_excel}"
    )

    mensaje.attach(parte_excel)

    # ==========================
    # ADJUNTAR PDF
    # ==========================

    with open(nombre_pdf, "rb") as adjunto_pdf:

        parte_pdf = MIMEBase(
            "application",
            "octet-stream"
        )

        parte_pdf.set_payload(
            adjunto_pdf.read()
        )

    encoders.encode_base64(parte_pdf)

    parte_pdf.add_header(
        "Content-Disposition",
        f"attachment; filename={nombre_pdf}"
    )

    mensaje.attach(parte_pdf)

    # ==========================
    # ENVIAR CORREO
    # ==========================

    try:

        servidor = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        servidor.starttls()

        servidor.login(
            correo_emisor,
            password
        )

        servidor.send_message(
            mensaje
        )

        servidor.quit()

        print(
            f"Correo enviado a: {correo_destino}"
        )

        registro_envios.append([
            fila["Nombre"],
            correo_destino,
            "Enviado",
            datetime.now()
        ])

    except Exception as e:

        print(
            f"Error con {correo_destino}: {e}"
        )

        registro_envios.append([
            fila["Nombre"],
            correo_destino,
            "Error",
            datetime.now()
        ])

# ==========================
# REPORTE FINAL
# ==========================

reporte = pd.DataFrame(
    registro_envios,
    columns=[
        "Nombre",
        "Correo",
        "Estado",
        "Fecha"
    ]
)

reporte.to_excel(
    "reporte_envios.xlsx",
    index=False
)

print("Proceso terminado correctamente")
print("Reporte generado: reporte_envios.xlsx")