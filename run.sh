#!/bin/bash

source src/datasets/mysql/credentials/cred.cred

dataset_path1='data/datasets/countries/'
dataset_path2='data/datasets/disasters/'


#load data sources
echo '##################### Uploading data on database ##################'
# python src/datasets/mysql/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path1

# python src/datasets/mysql/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path2


# run Easy RML
# http://localhost:5000/

echo '##################### Runnning all docker services ##################'
docker-compose down &&
docker-compose up -d &&
docker ps

#dragoman
echo '##################### Execution of Dragoman for functions mappings ##################'
docker exec -it coypu_demo_dragoman cp /src/mappings_and_config/configs_func/dragoman_func/functions.py /app/Interpreter/
curl localhost:6000/mapping_transformation/knowledge_graph/kg_creation/concepts/countries/configs/config_func.ini


#Sdm-rdfizer
echo '##################### Execution of Sdm-rdfizer for transformation in RDF KG ##################'
# time python -m rdfizer -c ./knowledge_graph/kg_creation/concepts/countries/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph/kg_creation/concepts/countries/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph/kg_creation/concepts/disasters/configs/config.ini
docker exec -it coypu_demo_semantic_enrichment python3 -m rdfizer -c /knowledge_graph/kg_creation/concepts/countries/configs/config.ini
docker exec -it coypu_demo_semantic_enrichment python3 -m rdfizer -c /knowledge_graph/kg_creation/concepts/disasters/configs/config.ini

echo '##################### Uploading RDF data files to triple store ##################'
./run_copy_all.sh


#graph-db

#valsparql
# http://localhost:5001/validate
# http://localhost:15000/sparql

#redash dashboard
# https://labs.tib.eu/sdm/coypu-endpoint/sparql

#general
#docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id

