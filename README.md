# ElectroStore - Proyecto Django

ElectroStore es una aplicación web desarrollada con Django que simula un sistema de tienda en línea.

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS

## Funcionalidades

- Gestión de productos
- Panel administrativo
- Base de datos integrada
- Sistema estructurado con Django

## Configuración de la base de datos

Este proyecto no incluye datos precargados ni una base de datos lista para usar.

Cada usuario debe:
1. Tener MySQL instalado y en ejecución.
2. Crear una base de datos local.
3. Configurar las credenciales de la base de datos en el archivo settings.py.
4. Ejecutar las migraciones para crear las tablas:

python manage.py migrate

Una vez realizadas las migraciones, los datos (productos, categorías, etc.) deben ser creados manualmente desde el panel administrativo o mediante registros propios.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

   git clone https://github.com/FiorellaMercado/DjangoProject.git

2. Entrar al proyecto:

   cd DjangoProject

3. Ejecutar el servidor:

   python manage.py runserver

4. Abrir en el navegador:

   http://127.0.0.1:8000/


## Autora

Fiorella Mercado

## Nota

Este enfoque es habitual en proyectos académicos y de desarrollo, donde la estructura del sistema se comparte mediante migraciones, pero los datos se gestionan de forma local.
