Comida al Paso - 
Backend APIAPI RESTful desarrollada con Django y Django REST Framework para gestionar el sistema de pedidos y menú del restaurante "Comida al Paso".

Tecnologías y Lenguaje: Python 3.10+Framework: Django 5.xAPI: Django REST Framework (DRF).

Autenticación: JWT (Simple JWT)

Base de Datos: SQLite (Desarrollo) / PostgreSQL (Producción)

CORS: django-cors-headersServidor Estático: WhiteNoise

Instalación y Configuración

Sigue estos pasos para levantar el servidor localmente:

1. Clonar el repositorioClona este repositorio en tu máquina local y accede a la carpeta del backend.

2. Crear entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias.Windowspython -m venv venv.\venv\Scripts\activateMac/Linuxpython3 -m venv venvsource venv/bin/activate

3. Instalar dependencias

Instala todas las librerías necesarias listadas en el archivo requirements.txt.pip install -r requirements.txt.

4. Configurar Base de Datos

Ejecuta las migraciones para crear las tablas en la base de datos (SQLite por defecto).python manage.py migrate. 

5. Cargar Datos Iniciales
Este proyecto incluye un script para poblar la base de datos con productos de ejemplo.python manage.py load_menu_data6.

6. Crear Administrador:
Para acceder al panel de administración y gestionar productos desde el frontend, 
logueate como admin, admin123
7. Ejecutar Servidor:
Inicia el servidor de desarrollo.python manage.py runserver
El servidor estará disponible en http://127.0.0.1:8000/

Endpoints Principales:
POST /api/token/ : Obtener token de acceso (Login)
POST /api/token/refresh/ : Refrescar token
GET /api/productos/ : Listar productos (soporta paginación)POST /api/comprar/ : Procesar orden de compraDespliegue

Este proyecto está configurado para desplegarse en plataformas como Render.

El archivo settings.py incluye configuración dinámica para base de datos (PostgreSQL/SQLite) y manejo de archivos estáticos con WhiteNoise.