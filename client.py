import threading
import os
from consumer import consumer
from producer import producer, send_data
from db_mongo import MongoDB

KAFKA1 = os.getenv('KAFKA_BROKER1')
TOPIC = os.getenv('TOPIC')

if __name__ == "__main__":
    client_name = input("What is your name? ")
    topic_name = input("What topic you want to subscribe? ")
    
    # envia nuevo topic a mongodb
    channel = MongoDB().add_channel(topic_name)
    print(channel)

    send_data(client_name,KAFKA1,topic_name, "\n"+client_name + " has entered the room\n")
    background_thread = threading.Thread(target=consumer, args=(KAFKA1,topic_name))
    background_thread.start()
    producer(client_name,KAFKA1,topic_name)
