# Sistema de Chat Utilizando Apache Kafka y MongoDB

Este proyecto implementa un "sistema de chat" en consola utilizando Apache Kafka para la mensajería y MongoDB para el almacenamiento persistente de mensajes. La aplicación está desarrollada en Python y se gestiona en contenedores Docker para facilitar la configuración y el despliegue.

## Estructura del Proyecto

El directorio del proyecto contiene los siguientes archivos y directorios:

- **Dockerfile**: Archivo para la creación de la imagen Docker de la aplicación.
- **app.py**: Punto de entrada principal de la aplicación que gestiona la interfaz de consola y las interacciones con Kafka y MongoDB.
- **client.py**: Módulo que contiene funciones para la gestión del cliente, incluyendo la selección de canales, envío y recepción de mensajes.
- **producer.py**: Módulo para la gestión de la producción y envío de mensajes a Kafka.
- **consumer.py**: Módulo para la gestión de la recepción y visualización de mensajes desde Kafka.
- **db_mongo.py**: Módulo para la gestión de la base de datos MongoDB, incluyendo la conexión y operaciones CRUD.

## Uso de la Aplicación

Para utilizar la aplicación:

1. Asegúrate de tener Docker instalado en tu sistema.
2. Clona este repositorio en tu máquina local.
3. Configura las variables de entorno necesarias para Kafka y MongoDB en el archivo `docker-compose.yml` y en los módulos de Python según sea necesario.
4. Ejecuta `docker-compose up --build` para iniciar los contenedores de Kafka, MongoDB y la aplicación.
5. Ejecuta `python3 client.py` en otra terminal para interactuar con la aplicación de chat.

## Arquitectura del Sistema y Decisiones de Diseño

El sistema se basa en una arquitectura cliente-servidor utilizando Apache Kafka como broker para la mensajería y MongoDB como base de datos para el almacenamiento de mensajes. La comunicación entre componentes se realiza mediante productores y consumidores de Kafka.

### Funcionamiento de Kafka y MongoDB

- **Apache Kafka**: Se utiliza para la publicación y suscripción de mensajes a través de topics. Los productores envían mensajes a topics específicos y los consumidores reciben mensajes de los topics a los que están suscritos.
  
- **MongoDB**: Se emplea para almacenar todos los mensajes enviados y recibidos. Cada mensaje se guarda como un documento con información relevante como autor, contenido y timestamp.

## Dependencias

- Python 3.x
- Docker
- Librerías Python: `kafka-python`, `pymongo`
