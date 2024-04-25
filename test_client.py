from multiprocessing import Process
import os
import time
KAFKA1 = os.getenv('KAFKA_BROKER1')
TOPIC = os.getenv('TOPIC')

if __name__ == "__main__":
    while True:
        time.sleep(5) 