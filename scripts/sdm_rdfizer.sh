#!/bin/bash

# time python -m rdfizer -c ./knowledge_graph/kg_creation/concepts/countries/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph/kg_creation/concepts/countries/configs/config.ini
# curl localhost:4000/graph_creation/knowledge_graph/kg_creation/concepts/disasters/configs/config.ini
docker exec -it coypu_demo_semantic_enrichment python3 -m rdfizer -c /knowledge_graph/kg_creation/concepts/countries/configs/config.ini
docker exec -it coypu_demo_semantic_enrichment python3 -m rdfizer -c /knowledge_graph/kg_creation/concepts/disasters/configs/config.ini