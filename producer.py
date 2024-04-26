from kafka import KafkaProducer
import time
from db_mongo import MongoDB


def delivery_report(err, msg):
    if err:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def producer(client_name, broker1, topic): #broker2, broker3,
    while True:
        data = input(client_name + " : ")
        if (data == "/exit"):
            break
        else:
            send_data(client_name, broker1, topic, data)
            time.sleep(2) 
    

def send_data(client_name, broker1, in_topic, msg):
    MongoDB().add_message(in_topic, client_name, msg)
    p = KafkaProducer(bootstrap_servers=broker1)
    formated_msg = client_name + " : " + msg
    p.send(topic=in_topic, value=formated_msg.encode(encoding='utf8'))
    p.close()
    

