from multiprocessing import Process
import os
from consumer import consumer
from producer import producer

KAFKA1 = os.getenv('KAFKA_BROKER1')
KAFKA2 = os.getenv('KAFKA_BROKER2')
KAFKA3 = os.getenv('KAFKA_BROKER3')
TOPIC = os.getenv('TOPIC')

if __name__ == "__main__":
    p1 = Process(target=producer('Tyler',KAFKA1,KAFKA2,KAFKA3,TOPIC))
    p1.start()
    p2 = Process(target=consumer(KAFKA1,KAFKA2,KAFKA3,TOPIC))
    p2.start()
    p1.join()
    p2.join()