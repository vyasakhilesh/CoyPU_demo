# CoyPu
## CoyPU KG creation, validation and exploration
Data sources, EasyRML, mappings rules, mapping functions, transformation, graphdb
Sparql endpoints, redash-dashboard, valSparql, Detrusty

# Project template for Knowledge graph creation, exploration and validation

## Data Sources (SQL, CSV etc.)

### Datasets

Load data (e.g. Emdat, GDACS, GlobalDisaster and Country Data) (e.g. ./data/)


## Create Mapping Files and Knowledge Graph Creation 

 * Steps:
    
    ### Run (e.g. ./run.sh) to run all docker containers and execute complete pipeline 
   
    ### Or Run each component separately

      1. Create Mapping file using [RML](https://rml.io/specs/rml/) or [easyRML](https://github.com/SDM-TIB/easyRML) http://localhost:5000/
      2. Add function in mapping file (RML+FnO) (e.g. knowledge_graph_creation/mappings/countries.ttl)
         a. Add function definition in python script (e.g. knowledge_graph_creation/mapping_funcs/functions.py)
      3. Add [config]((https://github.com/SDM-TIB/Dragoman)) file for the translation of mapping file into functions-free mapping file (RML only)
         (e.g. knowledge_graph_creation/mappings/configs/config_func.ini)
      4. Run [Dragoman](https://github.com/SDM-TIB/Dragoman) (e.g. ./knowledge_graph_creation/dragoman.sh) for function free mapping files 
         
         From [PyPI](https://pypi.org/project/dragoman-tool/)
         ```
          python3 -m pip install dragoman-tool
          python3 -m Interpreter -c knowledge_graph_creation/configs/config_func.ini

         ```
         
         From [Docker](https://hub.docker.com/repository/docker/sdmtib/dragoman) (e.g. ./docker-compose.yml)
         ```
          # copying function file to docker container of Dragoman
          docker exec -it dragoman cp /knowledge_graph_creation/mapping_funcs/functions.py /app/Interpreter/

          # translate mapping file (with function) into function-free mapping file
          curl localhost:6000/mapping_transformation/knowledge_graph_creation/configs/config_func.ini
          
          # Copying function-free mapping files into mapping folder
          cp data/translated/*.ttl knowledge_graph_creation/mappings/
         ```
      5. Add [config](https://github.com/SDM-TIB/SDM-RDFizer/wiki/The-Parameters-of-the-Configuration-file) file to interpret mapping file (without functions) (e.g. knowledge_graph_creation/mappings/configs/config.ini)
      6. Run [SDM-RdFizer](https://github.com/SDM-TIB/SDM-RDFizer) (e.g. ./knowledge_graph_creation/sdm_rdfizer.sh) to interpret mapping files and transformation of data sources into RDF Knowlede graph
          
          From PyPI [Link](https://pypi.org/project/rdfizer/):
          ```
          python3 -m pip install rdfizer
          python3 -m rdfizer -c /knowledge_graph_creation/configs/config.ini
          ```
          
          From [Docker](https://github.com/SDM-TIB/SDM-RDFizer/wiki/Install&Run) (e.g. ./docker-compose.yml)
          ```
          docker exec -it semantic_enrichment python3 -m rdfizer -c /knowledge_graph_creation/configs/config.ini

          ```





