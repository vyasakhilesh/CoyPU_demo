#!/bin/bash

# Copy Grphs data
echo '#####################Copying Graphs Data##################'
find data_gen/graphs/concepts/ -name '*.nt' -exec cp -t data_gen/graphs/all_graphs {} +

echo '#####################Copying Shapes Data##################'
find knowledge_graph/kg_validation/concepts/ -name '*.json' -exec cp -t knowledge_graph/kg_validation/all_shapes {} +

echo '##################### Backing-up Graphs Data on Triple Store ##################'
ssh node2 'cp /data/coypu/sparql_endpoint/data_load/*.nt /data/coypu/sparql_endpoint/data_backup/'

echo '#####################Copying Graphs Data to Triple Store ##################'
rsync -avP data_gen/graphs/all_graphs/*.nt node2:/data/coypu/sparql_endpoint/data_load

# for deleting files from remote side which are not on local side
#rsync -avP --delete data_gen/graphs/all_graphs/*.nt node2:/data/coypu/sparql_endpoint/data_load




