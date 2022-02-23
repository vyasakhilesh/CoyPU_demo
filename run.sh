#!/bin/bash

#load data sources
echo '##################### Uploading data on database ##################'
while true; do
    read -p "Do you wish to upload data on database?" yn
    case $yn in
        [Yy]* ) ./scripts/load_data.sh; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done



# run Easy RML
# http://localhost:5000/

echo '##################### Runnning all docker services ##################'
while true; do
    read -p "Do you wish to run docker services?" yn
    case $yn in
        [Yy]* ) docker-compose down; docker-compose up -d; docker ps; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


#dragoman
echo '##################### Execution of Dragoman for functions mappings ##################'
./scripts/dragoman.sh

#Sdm-rdfizer
echo '##################### Execution of Sdm-rdfizer for transformation in RDF KG ##################'
./scripts/sdm_rdfizer.sh

echo '##################### Uploading data files to all folder ##################'
while true; do
    read -p "Do you wish to upload RDF data files and validation files to all folder?" yn
    case $yn in
        [Yy]* ) ./scripts/run_copy_all.sh; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done



#graph-db

#valsparql
# http://localhost:5001/validate
# http://localhost:15000/sparql

#redash dashboard
# https://labs.tib.eu/sdm/coypu-endpoint/sparql

#general
#docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id

echo '##################### Backing-up Graphs Data on Triple Store ##################'
ssh node2 'cp /data/coypu/sparql_endpoint/data_load/*.nt /data/coypu/sparql_endpoint/data_backup/'

echo '#####################Copying Graphs Data to Triple Store ##################'
rsync -avP data_gen/graphs/all_graphs/*.nt node2:/data/coypu/sparql_endpoint/data_load

# for deleting files from remote side which are not on local side
#rsync -avP --delete data_gen/graphs/all_graphs/*.nt node2:/data/coypu/sparql_endpoint/data_load

echo '##################### Setting up docker for CoyPU sparql endpoint##################'
echo '##################### Uploading RDF data files to triple store ##################'
while true; do
    read -p "Do you wish to upload RDF data files to triple store?" yn
    case $yn in
        [Yy]* ) scp ./docker_command.sh node2://data/coypu/sparql_endpoint/;
                ssh node2 'cd /data/coypu/sparql_endpoint/ && ./docker_command.sh >out 2>error &';
                sleep 60s;
                ssh node2 'cat /data/coypu/sparql_endpoint/out || cat /data/coypu/sparql_endpoint/error';
                break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


