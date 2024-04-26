from kafka import KafkaConsumer
from db_mongo import MongoDB

def error_cb(err):
    print('Error: %s' % err)

def consumer(broker1, topic):
    c = KafkaConsumer(topic, bootstrap_servers=broker1)
    past_messages = MongoDB().get_messages_by_channel(topic)
    for message in past_messages:
        print(message["author"]+ " : "+ message["message"])
    while True:
        try:
            for msg in c:
                value = msg[6].decode()
                print(value)
        except KeyboardInterrupt:
            c.close()
            break