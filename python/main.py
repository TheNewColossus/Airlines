# -*- coding: utf-8 -*-

import subprocess
import sys
import time

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
  __import__("kafka-python-ng")
except ImportError:
  install("kafka-python-ng")
finally:
  from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="broker:29092", 
    client_id='Airlines_group'
)

topic_list = []
topic_list.append(NewTopic(name="Airlines_Data", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

i = 0
while True:
  print(i)
  i += 1
  time.sleep(2)


