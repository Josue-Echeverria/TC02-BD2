from pymongo import MongoClient
from datetime import datetime
import os


config = {
    "host": os.getenv("MONGO_HOST"), 
    "port": int(os.getenv("MONGO_PORT")), 
    "username": os.getenv("MONGO_USER"),
    "password": os.getenv("MONGO_PASSWORD"),
    "database": os.getenv("MONGO_DB")
}


class MongoDB:
    def __init__(self):
        client = MongoClient(
            host=config["host"],
            port=config["port"],
            username=config["username"],
            password=config["password"]
        )
        self.db = client[config["database"]]

    def add_channel(self, channel_name):
        '''
        Agrega un nuevo canal a la base de datos.

        Parameters:
            channel_name (str): Nombre del canal que se desea agregar

        Returns:
            result (str): Un mensaje indicando el éxito de la operación o un error si algo salió mal
        '''
        try:
            self.db.channels.insert_one({"channel": channel_name, "messages": []})
            return f"Canal '{channel_name}' agregado exitosamente."
        except Exception as e:
            return f"Error al agregar el canal: {str(e)}"

    def list_channels(self):
        '''
        Lista todos los canales almacenados en la base de datos.

        Returns:
            channels (list): Lista de nombres de canales
        '''
        channels = [channel["channel"] for channel in self.db.channels.find()]
        return channels

    def add_message(self, channel_name, author, message):
        '''
        Agrega un nuevo mensaje al canal especificado en la base de datos.

        Parameters:
            channel_name (str): Nombre del canal al que se desea agregar el mensaje
            author (str): Nombre del autor del mensaje
            message (str): Contenido del mensaje

        Returns:
            result (str): Un mensaje indicando el éxito de la operación o un error si algo salió mal
        '''
        try:
            message_data = {"author": author, "message": message, "timestamp": datetime.now().strftime("%d de %B a las %H:%M")}
            self.db.channels.update_one({"channel": channel_name}, {"$push": {"messages": message_data}})
            return "Mensaje agregado exitosamente."
        except Exception as e:
            return f"Error al agregar el mensaje: {str(e)}"

    def get_messages_by_channel(self, channel_name):
        '''
        Obtiene todos los mensajes para el canal especificado.

        Parameters:
            channel_name (str): Nombre del canal del que se desean obtener los mensajes

        Returns:
            messages (list): Lista de mensajes para el canal dado
        '''
        messages = self.db.channels.find_one({"channel": channel_name}, {"_id": 0, "messages": 1})
        if messages:
            return messages["messages"]
        else:
            return []
