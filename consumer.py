from kafka import KafkaConsumer


def error_cb(err):
    print('Error: %s' % err)

def consumer(broker1, topic):
    c = KafkaConsumer(topic, bootstrap_servers=broker1)
    while True:
        for msg in c:
            topic = msg[0]
            value = msg[6]
            print(msg)
            print(f"{topic}:{value.decode()}")
       