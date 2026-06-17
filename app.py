import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

correo_emisor = "[TU_CORREO@gmail.com](mailto:TU_CORREO@gmail.com)"
password = "TU_CONTRASEÑA_DE_APLICACION"

df = pd.read_excel("clientes.xlsx")

registro_envios = []

for _, fila in df.iterrows():
  correo_destino = fila["Correo"]

mensaje = MIMEMultipart()

mensaje["From"] = correo_emisor
mensaje["To"] = correo_destino
mensaje["Subject"] = "Información de Producto"

cuerpo = f"""
```

Hola {fila['Nombre']},

Le informamos que su producto asignado es:

{fila['Producto']}

Gracias por su atención.

Saludos cordiales.
"""

mensaje.attach(
    MIMEText(cuerpo, "plain"))

try:

    servidor = smtplib.SMTP(
        "smtp.gmail.com",
        587)

    servidor.starttls()

    servidor.login(
        correo_emisor,
        password)

    servidor.send_message(
        mensaje)

    servidor.quit()

    print(f"Correo enviado a {correo_destino}")

    registro_envios.append([
        fila["Nombre"],
        correo_destino,
        "Enviado",
        datetime.now()])

except Exception as e:

    print(f"Error con {correo_destino}: {e}")

    registro_envios.append([
        fila["Nombre"],
        correo_destino,
        "Error",
        datetime.now()
    ])
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

print("Proceso terminado")
print("Reporte generado")
