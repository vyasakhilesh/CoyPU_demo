#!/bin/bash

docker exec -it coypu_demo_dragoman cp /src/mappings_and_config/configs_func/dragoman_func/functions.py /app/Interpreter/

curl localhost:6000/mapping_transformation/knowledge_graph/kg_creation/concepts/countries/configs/config_func.ini
