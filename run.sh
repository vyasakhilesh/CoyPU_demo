source ./db/cred.cred
dataset_path=''


python db/csv2dbs.py --host=$host --port=$port --pwd=$pwd --uname=$uname --dbname=$dbname -i=$dataset_path


# run Easy RML
# http://localhost:5000/

# time python -m rdfizer -c ./knowledge_graph/kg_creation/countries/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph/kg_creation/countries/configs/config.ini
# curl localhost:6000/mapping_transformation/knowledge_graph/kg_creation/countries/configs/config_func_csv.ini



