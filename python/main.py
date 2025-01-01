# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time
import json

def install(package):
  # Installing a package 
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Checking if kafka-python library is installed
try:
  __import__("kafka-python-ng")
except ImportError:
  install("kafka-python-ng")
  install("requests")
finally:
  from kafka.admin import KafkaAdminClient, NewTopic
  from kafka import KafkaProducer
  import requests

# Creating a kafka topic
admin_client = KafkaAdminClient(
    bootstrap_servers="broker:29092"
)

topic_list = []
topic_list.append(NewTopic(name="Airlines_Data", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Creating a kafka producer
producer = KafkaProducer(bootstrap_servers=['broker:29092'],value_serializer=lambda m: json.dumps(m).encode('ascii'))

# Got the access key from an api
params = {
  'access_key': os.environ["api_key"]
}

while True:
  # Sending request to the api
  api_result = requests.get('https://api.aviationstack.com/v1/flights', params)
  api_response = api_result.json()

  # Received the response
  for flight in api_response['data']:
    # Sending data through the producer
    producer.send("Airlines_Data",flight)
    # Flushing it after one iteration
    producer.flush()

  # Preparing for the next batch
  time.sleep(100)
        