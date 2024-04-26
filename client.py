import os
from consumer import consumer
from producer import producer, send_data
from db_mongo import MongoDB

KAFKA1 = os.getenv('KAFKA_BROKER1')


def menu():
    print("\n1. Seleccionar topic")
    print("2. Enviar mensajes")
    print("3. Leer mensajes")
    print("4. Salir")


def select_channel(client_name, kafka_broker, topic):
    topic = input("Ingrese el nombre del topic: ")
    MongoDB().add_channel(topic)
    send_data("sistema",kafka_broker,topic, client_name + " se ha conectado")
    print("\nTe has conectado al topic " + topic)
    print("Cuando desee de cambiar de topic solo vuelva al menu principal y vuelva a seleccionar topic" +"\n")
    return topic


def send_messages(client_name, kafka_broker, topic):
    if topic == "":
        print("\nPrimero seleccionar un topic\n")
    else:
        print("\nAhora puedes enviar mensajes al topic " + topic)
        print("Para salir regresar al menu principal escriba /exit" +"\n")
        producer(client_name, kafka_broker, topic)


def receive_messages(topic):
    if topic == "":
        print("\nPrimero seleccionar un topic\n")
    else:
        print("\nAhora estas recibiendo mensajes del topic " + topic)
        print("Para salir al menu principal digite [Ctrl + c]\n")
        consumer(KAFKA1,topic)


def disconnect_client(client_name, kafka_broker, topic):
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
        if option == '1':
            topic = select_channel(client_name, KAFKA1, topic)
        elif option == '2':
            send_messages(client_name, KAFKA1, topic)
        elif option == '3':
            receive_messages(topic)
        elif option == '4':
            disconnect_client(client_name, KAFKA1, topic)
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

