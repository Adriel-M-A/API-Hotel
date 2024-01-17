# Backend

## Requisitos Previos

- [Python](https://www.python.org/) (Versión 3.11.4)

## Configuración de Entorno

### 1. Accede a la carpeta `backend` dentro del repositorio clonado:

```
cd backend
```

### 2. Crea y activa el entorno virtual

```
python -m venv venv
```

- Activación en sistemas Windows:

```
venv\Scripts\activate
```

- Activación en sistemas Linux o Mac:

```
source venv/bin/activate
```

### 3. Instala las dependencias del proyecto desde el archivo requirements.txt:

```
pip install -r requirements.txt
```

### 4. Configuración de Postgresql

Para configurar el entorno local, se necesita crear un archivo `.env` y añadir las variables de entorno.

```
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=nombre_de_la_db
DATABASE_USER=nombre_del_usuario (por defecto, suele ser "postgres")
DATABASE_PASSWORD=contraseña
DATABASE_HOST=localhost
DATABASE_PORT=5432 (por defecto, el puerto suele ser 5432)
SECRET_KEY=
```

### 5. Crear migraciones

```
python manage.py makemigrations
```

```
python manage.py migrate
```

### 6. Cargar datos de "prueba" en la base de datos

- Cargar todos los datos:

```
python manage.py loaddata_all
```

- Cargar datos individualmente (en caso de que ya se tengan datos cargados) utilizar solo el que sea necesario:

```
python manage.py loaddata core/fixtures/data.json
```

```
python manage.py loaddata hotel/fixtures/data.json
```

### 7. Crear super usuario

```
python manage.py createsuperuser
```

### 8. Ejecutar el Servidor

```
python manage.py runserver
```
