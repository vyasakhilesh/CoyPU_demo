source src/datasets/mysql/credentials/cred.cred

dataset_path1='data/datasets/countries/'
dataset_path2='data/datasets/disasters/'


#load data sources
python src/datasets/mysql/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path1

python src/datasets/mysql/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path2


# run Easy RML
# http://localhost:5000/


#Sdm-rdfizer
# time python -m rdfizer -c ./knowledge_graph/kg_creation/countries/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph/kg_creation/countries/configs/config.ini
# docker exec -it coypu_demo_semantic_enrichment python3 -m rdfizer -c /knowledge_graph/kg_creation/countries/configs/config.ini


#dragoman
# docker exec -it coypu_demo_dragoman cp /src/mappings_and_config/configs_func/dragoman_func/functions.py /app/Interpreter/
# # curl localhost:6000/mapping_transformation/knowledge_graph/kg_creation/countries/configs/config_func_csv.ini

#graph-db

