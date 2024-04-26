import os
from consumer import consumer
from producer import producer, send_data
from db_mongo import MongoDB

KAFKA1 = os.getenv('KAFKA_BROKER1')


def menu():
    '''
    Imprime en la terminal las opciones que tiene el usuario

    Returns:
        result (): Opciones que tiene el usuario en la terminal
    '''
    print("\n1. Seleccionar topic")
    print("2. Enviar mensajes")
    print("3. Leer mensajes")
    print("4. Salir")


def select_channel(client_name, kafka_broker, topic):
    '''
    Funcion llamada cuando el cliente elige la opcion de conectarse a un topic

    Parameters:
        client_name (str): Nombre del cliente
        kafka_broker (str): Direccion del broker ("host : port")
        topic (str): Topic/canal al que se desea conectar

    Returns:
        result (str): Topic/canal al que se conecto el cliente
    '''
    topic = input("Ingrese el nombre del topic: ")
    MongoDB().add_channel(topic)

    # Registra la conexion al topic al topic del broker
    send_data("sistema",kafka_broker,topic, client_name + " se ha conectado") 
    print("\nTe has conectado al topic " + topic)
    print("Cuando desee de cambiar de topic solo vuelva al menu principal y vuelva a seleccionar topic" +"\n")
    return topic


def send_messages(client_name, kafka_broker, topic):
    '''
    Funcion llamada cuando el cliente elige la opcion de enviar mensajes del topic seleccionado en la opcion 1

    Parameters:
        client_name (str): Nombre del cliente
        kafka_broker (str): Direccion del broker ("host : port")
        topic (str): Topic/canal al que se desea enviar mensajes

    Returns:
        result (): Nada en caso que no haya especificado el topic
        result (): Conexion como producer al topic seleccionado
    '''
    if topic == "":
        print("\nPrimero seleccionar un topic\n")
    else:
        print("\nAhora puedes enviar mensajes al topic " + topic)
        print("Para salir regresar al menu principal escriba /exit" +"\n")
        producer(client_name, kafka_broker, topic)


def receive_messages(topic):
    '''
    Funcion llamada cuando el cliente elige la opcion de recibir mensajes del topic seleccionado en la opcion 1

    Parameters:
        topic (str): Topic/canal al que se desea conectar

    Returns:
        result (): Nada en caso que no haya especificado el topic
        result (): Conexion como consumer al topic seleccionado
    '''
    if topic == "":
        print("\nPrimero seleccionar un topic\n")
    else:
        print("\nAhora estas recibiendo mensajes del topic " + topic)
        print("Para salir al menu principal digite [Ctrl + c]\n")
        consumer(KAFKA1,topic)


def disconnect_client(client_name, kafka_broker, topic):
    '''
    Funcion llamada cuando el cliente elige la opcion de salir del app

    Parameters:
        client_name (str): Nombre del cliente
        kafka_broker (str): Direccion del broker ("host : port")
        topic (str): Topic/canal al que el cliente estaba conectado

    Returns:
        result (): Registro de desconexion en la base de datos 
    '''
    if topic != "":
        send_data("sistema",kafka_broker,topic, client_name + " se ha desconectado")
    print("\nGracias por elegirnos\n")


if __name__ == "__main__":
    print("\nBienvenid@ a la mejor app de chat implementando kafka")
    client_name = input("Cual es tu nombre? ")
    topic = ""
    while True:
        menu()
        option = input("Seleccione una opción: ")

        # Seleccionar topic
        if option == '1':
            topic = select_channel(client_name, KAFKA1, topic)
    
        # Enviar mensajes
        elif option == '2':
            send_messages(client_name, KAFKA1, topic)
        
        # Recibir mensajes
        elif option == '3':
            receive_messages(topic)

        # Salir
        elif option == '4':
            disconnect_client(client_name, KAFKA1, topic)
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

