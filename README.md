# 📧 Sistema de Automatización de Correos y Reportes Analíticos (RPA)

Aplicación web desarrollada en Python y Streamlit diseñada para automatizar flujos de comunicación masiva y personalizada a partir de bases de datos en Excel. Optimiza procesos operativos (como el envío de facturas, estados de cuenta, órdenes de compra o reportes de producción), eliminando las tareas manuales repetitivas y garantizando un registro analítico de cada envío.

![Interfaz del Proyecto](images/inicio.png) <!-- Asegúrate de tener una captura aquí si aplica -->

## 🚀 Funcionalidades Clave
*   **Ingesta de Datos Inteligente:** Carga y procesamiento dinámico de archivos Excel sin importar el volumen de registros.
*   **Hiper-Personalización:** Generación de cuerpos de correo dinámicos que adaptan automáticamente nombres, saldos, fechas u otros datos específicos por cliente.
*   **Gestión de Adjuntos Automatizada:** Vinculación e inclusión automática de archivos adjuntos específicos para cada destinatario.
*   **Dashboard de Control:** Visualización interactiva en tiempo real de los datos cargados antes de ejecutar el envío.
*   **Módulo de Auditoría y Reportes:** Descarga automática de un informe final consolidado que detalla el estado de cada envío (Éxito/Error) para garantizar la trazabilidad.

## 🏭 Casos de Uso en Producción y Logística (Tu enfoque diferenciador)
*   **Gestión de Proveedores:** Automatización del envío de órdenes de compra y solicitudes de cotización masivas a proveedores logísticos.
*   **Control de Calidad:** Notificación automática a diferentes áreas de la planta sobre los reportes de defectos, métricas de productividad o alertas de mantenimiento.

## 🛠️ Stack Tecnológico
*   **Core Language:** Python 3.x
*   **Procesamiento de Datos:** Pandas & OpenPyXL (Manipulación y lectura eficiente de dataframes y archivos Excel)
*   **Protocolo de Comunicación:** SMTP (Simple Mail Transfer Protocol con librerías nativas de Python para conexiones seguras SSL/TLS)
*   **Interfaz de Usuario:** Streamlit (UI intuitiva para usuarios no técnicos)

## 🔄 Flujo de Trabajo del Sistema (Pipeline)
1.  **Carga (Upload):** El usuario arrastra el archivo `.xlsx` o `.xls` a la plataforma.
2.  **Validación visual:** El sistema renderiza una tabla interactiva para auditar los datos antes del envío.
3.  **Procesamiento y Envío:** Un bucle optimizado recorre la base de datos, construye los correos, adjunta los archivos correspondientes y los despacha mediante el servidor SMTP.
4.  **Conciliación:** El sistema genera un reporte final con métricas de éxito del proceso para su descarga inmediata.

## 👩‍💻 Autora
**Cielo Nichool Cuevas Perdomo**  
*Tecnóloga en Producción Industrial & Especialista en Ciencia de Datos e IA Generativa*
