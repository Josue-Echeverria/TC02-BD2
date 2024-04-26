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

5. Una vez que se tengan los 3 contenedores corriendo, se debe de adjuntar un shell al contenedor de client.

6. Ir al directorio /opt/app (Donde se copian los archivos de codigo en el contenedor).

7. Ejecutar `python client.py`. Para este punto ya tenemos nuestra interfaz de terminal en funcionamiento y lo primero que hara sera preguntar por el nombre del cliente:

```
# python client.py

Bienvenid@ a la mejor app de chat implementando kafka
Cual es tu nombre? 
```
8. Una vez que se especifica el nombre del cliente la interfaz despliega las opciones que tiene el cliente dentro la aplicación

```
# python client.py 

Bienvenid@ a la mejor app de chat implementando kafka
Cual es tu nombre? Josue

1. Seleccionar topic
2. Enviar mensajes
3. Leer mensajes
4. Salir
Seleccione una opción:
```
9. Para que el cliente pueda realizar las opciones 2 y 3 primero debera de seleccionar el topic al que se desea conectar eligiendo la opción 1
```
# python client.py

Bienvenid@ a la mejor app de chat implementando kafka
Cual es tu nombre? Josue

1. Seleccionar topic
2. Enviar mensajes
3. Leer mensajes
4. Salir
Seleccione una opción: 1
Ingrese el nombre del topic: GrupoBases2

Te has conectado al topic GrupoBases2
Cuando desee de cambiar de topic solo vuelva al menu principal y vuelva a seleccionar topic


1. Seleccionar topic
2. Enviar mensajes
3. Leer mensajes
4. Salir
Seleccione una opción: 
```
10. Si el cliente desea enviar mensajes en el topic seleccionado debe elegir la opcion 2. Esta opción abre un producer de kafka para que el usuario envie los mensajes que quiera al topic.
```
1. Seleccionar topic
2. Enviar mensajes
3. Leer mensajes
4. Salir
Seleccione una opción: 2

Ahora puedes enviar mensajes al topic GrupoBases2
Para salir regresar al menu principal escriba /exit

Josue : Esto es un mensaje de ejemplo enviado al topic
Josue : 
```

11. Si el cliente desea recibir mensajes en el topic seleccionado debe elegir la opcion 3. Esta opción abre un consumer de kafka para que el usuario reciba los mensajes del topic en tiempo real y tambien ver los mensajes enviados. 

```
1. Seleccionar topic
2. Enviar mensajes
3. Leer mensajes
4. Salir
Seleccione una opción: 3

Ahora estas recibiendo mensajes del topic GrupoBases2
Para salir al menu principal digite [Ctrl + c]

sistema : Josue se ha conectado
Josue : Esto es un mensaje de ejemplo
```

12. Cuando el cliente desee terminar la ejecucion del programa debe seleccionar la opcion 4, lo cual registra la desconexion del cliente enviando un mensaje al topic y guardandolo en la base de datos.


## Arquitectura del Sistema y Decisiones de Diseño

El sistema se basa en una arquitectura cliente-servidor utilizando Apache Kafka como broker para la mensajería y MongoDB como base de datos para el almacenamiento de mensajes. La comunicación entre componentes se realiza mediante productores y consumidores de Kafka.

### Funcionamiento de Kafka y MongoDB

- **Apache Kafka**: Se utiliza para la publicación y suscripción de mensajes a través de topics. Los productores envían mensajes a topics específicos y los consumidores reciben mensajes de los topics a los que están suscritos.
  
- **MongoDB**: Se emplea para almacenar todos los mensajes enviados y recibidos. Cada mensaje se guarda como un documento con información relevante como autor, contenido y timestamp.

## Dependencias

- Python 3.x
- Docker
- Librerías Python: `kafka-python`, `pymongo`
