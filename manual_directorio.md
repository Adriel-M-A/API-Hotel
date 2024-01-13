# Estructura del Proyecto

El proyecto backend está organizado en varias carpetas para facilitar la gestión y estructuración del código.

`api`:

- Contiene todo lo relacionado con Django Rest Framework.
- Archivos y carpetas específicos para vistas, serializadores, autenticación, etc.
- También incluye subcarpetas como "core", "hotel" y "venta".

---

`apps`:

- Contiene las aplicaciones Django, donde cada aplicación se enfoca en modelos específicos o funcionalidades del proyecto.
- Cada aplicación tiene su propio conjunto de modelos, vistas, migraciones, etc.
- Incluye subcarpetas como "core", "hotel" y "venta".

---

`project`:

- Es la carpeta principal del proyecto Django.
- Contiene configuraciones del proyecto, archivos de enrutamiento (urls.py), configuraciones de la base de datos, etc.

---

`venv`:

- Carpeta que almacena el entorno virtual del proyecto.
- Se utiliza para aislar las dependencias del proyecto y mantener la coherencia en las versiones de las bibliotecas.

## Descripción Detallada

> Tanto las carpetas api como apps contienen subcarpetas llamadas `core`, `hotel` y `venta`, las cuales están estructuradas de la siguiente manera:

`api`

- views: Contiene las vistas de Django Rest Framework, que definen la lógica para procesar las solicitudes HTTP.
- serializers: Almacena los serializadores utilizados para convertir objetos complejos, como consultas de base de datos, en tipos de datos de Python.

`apps`

- models: Define los modelos de datos para la aplicación.
- migrations: Almacena las migraciones de la base de datos generadas por Django.
- tests: Contiene pruebas específicas de la aplicación.

`project`

- settings: Archivo de configuración principal del proyecto Django.
- urls: Define las rutas y enlaces del proyecto.
