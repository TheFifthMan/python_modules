#!/usr/bin/env python 
#-*- coding:utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

producer = KafkaProducer(bootstrap_servers=['192.168.31.64:9092','192.168.31.64:9093','192.168.31.64:9094'],retries=5)

# Asynchronous by default
future = producer.send('my-topic', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

producer.send('my-topic',key=b'test',value=b'this is testing message')

producer2 = KafkaProducer(bootstrap_servers=['192.168.31.64:9092','192.168.31.64:9093','192.168.31.64:9094'],value_serializer=lambda m:json.dumps(m).encode('utf-8'))
producer2.send('json-files','{"keyxxxx":"valuexxx"}')
