Config:-
bootstrap_server = broker:29092
topic_name = Airlines_Data
Apache Druid URL = http://localhost:8081
Grafana Dashboard URL = http://localhost:3000
Druid-Grafna connection URL = http://broker:8082 

# Kindly wait for a couple of minutes for the docker cluster to be completely active.

# Sometimes the druid starts in an overlord mode so click on the yellow exclaimation mark
# on the dashboard title bar and click on "Start with SQL" option.

# Click on "Load Data" on the Druid titlebar to start ingesting streaming data from kafka
# Since the api data is in json format, choose json in the ingesting options.

# The default username and password for Grafana is admin, 
# but you may chose to create your own username and password. 

# If you are unable to ingest data from the api, it is possible that my endpoint has been exhausted.
# For that kindly signup at "Aviation Stack" api and get a new key and paste it in ".env" file here, though it is highly improbable for
# my endpoint to expire.