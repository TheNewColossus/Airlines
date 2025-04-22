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

# Waiting for kafka cluster to be up and running
time.sleep(100)

# Creating a kafka client
admin_client = KafkaAdminClient(
    bootstrap_servers="broker:29092"
)

# Creating the topic if it doesn't exist already
if "Airlines_Data" in admin_client.list_topics():
  pass
else:
  topic_list = []
  topic_list.append(NewTopic(name="Airlines_Data", num_partitions=1, replication_factor=1))
  admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Creating a kafka producer
producer = KafkaProducer(bootstrap_servers=['broker:29092'],value_serializer=lambda m: json.dumps(m).encode('ascii')\
,max_request_size=20971520,api_version = (2, 8, 0))

# Got the access key from an api
params = {
  'access_key': os.environ["api_key"]
}

# Transformation function to extract relevant data from the json response
from collections.abc import MutableMapping

def flatten(dictionary, parent_key='', separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)


# These are the response variables that are to be extracted from the API response.
variables = ['flight_date','flight_status','departure_airport','departure_timezone','departure_terminal','departure_scheduled',\
'departure_estimated','departure_delay','arrival_airport','arrival_timezone','arrival_terminal','arrival_scheduled',\
'arrival_estimated','arrival_delay']

while True:
  # Sending request to the api
  api_result = requests.get('https://api.aviationstack.com/v1/flights', params)
  api_response = api_result.json()

  # Received the response
  for flight in api_response['data']:
    
    #Transforming the data
    flt_flight = flatten(flight)
    pay_load = {var: flt_flight[var] if flt_flight[var] is not None else 'N/A' for var in variables}
    
    # Sending data through the producer
    producer.send("Airlines_Data",pay_load)
    # Flushing it after one iteration
    producer.flush()

  # Preparing for the next batch
  time.sleep(10)
        
