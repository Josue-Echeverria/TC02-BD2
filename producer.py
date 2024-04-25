from kafka import KafkaProducer
import time

def delivery_report(err, msg):
    if err:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def producer(client_name, broker1, topic): #broker2, broker3,
    
    while True:
        data = input(client_name + " : ")
        send_data(client_name, broker1, topic, "\n"+client_name + " : " + data)
        time.sleep(2) 

def send_data(client_name, broker1, Itopic, msg):
    
    p = KafkaProducer(bootstrap_servers=broker1)
    p.send(topic=Itopic, value=msg.encode(encoding='utf8'))
    p.close()
    