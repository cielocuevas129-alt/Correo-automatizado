import pandas as pd
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from datetime import datetime

# ==========================

# CONFIGURACION

# ==========================

correo_emisor = "[tucorreo@gmail.com](mailto:tucorrreo@gmail.com)"
password = "tu contraseña para la aplicaicon"

# ==========================

# LEER EXCEL CLIENTES

# ==========================

df = pd.read_excel("clientes.xlsx")

registro_envios = []

# ==========================

# RECORRER CLIENTES

# ==========================

for _, fila in df.iterrows():

    correo_destino = fila["Correo"]

    nombre_excel = f"Reporte_{fila['Nombre']}.xlsx"

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
# CREAR EXCEL PERSONALIZADO
# ==========================


# ==========================
# CREAR CORREO
# ==========================

mensaje = MIMEMultipart()

mensaje["From"] = correo_emisor
mensaje["To"] = correo_destino
mensaje["Subject"] = "Información de Producto"

cuerpo = f"""
```

Hola {fila['Nombre']},

Le informamos que su producto asignado es:

{fila['Producto']}

Adjuntamos su reporte personalizado.

Gracias por su atención.

Saludos cordiales.
"""


mensaje.attach(
    MIMEText(cuerpo, "plain")
)

# ==========================
# ADJUNTAR EXCEL
# ==========================

with open(nombre_excel, "rb") as adjunto:

    parte = MIMEBase(
        "application",
        "octet-stream"
    )

    parte.set_payload(
        adjunto.read()
    )

encoders.encode_base64(parte)

parte.add_header(
    "Content-Disposition",
    f"attachment; filename={nombre_excel}"
)

mensaje.attach(parte)

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
        f"Correo enviado a {correo_destino}"
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

# REPORTE GENERAL

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