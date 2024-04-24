from confluent_kafka import Consumer, KafkaException
import os

def error_cb(err):
    print('Error: %s' % err)

def consumer(broker1, broker2, broker3, topic):
    conf = {
        'bootstrap.servers':  broker1+','+broker2+','+broker3,
        'group.id': topic, 
        'auto.offset.reset': 'earliest', 
        'error_cb': error_cb,
    }
    c = Consumer(conf)
    c.subscribe([topic])

    try:
        while True:
            msg = c.poll(1.0)  
            if msg is None:
                # print("receiving")
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                print('Received message: %s' % msg.value().decode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        c.close()
