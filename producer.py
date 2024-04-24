from confluent_kafka import Producer


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def producer(client_name, broker1, broker2, broker3, topic):
    conf = {
        'bootstrap.servers': broker1+','+broker2+','+broker3  # change if your broker is on a different host
    }
    p = Producer(conf)
    while True:
        print()
        data = input({client_name} + ' : ')
        p.produce(topic, key=None, value=data, callback=delivery_report)
        p.flush()

