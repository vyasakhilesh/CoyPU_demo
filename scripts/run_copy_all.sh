#!/bin/bash

# Copy Graphs data
echo '#####################Copying Graphs Data ##################'
find data_gen/graphs/concepts/ -name '*.nt' -exec cp -t data_gen/graphs/all_graphs {} +

echo '#####################Copying Shapes Data ##################'
find knowledge_graph/kg_validation/concepts/ -name '*.json' -exec cp -t knowledge_graph/kg_validation/all_shapes {} +



