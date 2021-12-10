Execute the JAR file with the following command (where 'Ontology IRI' is the IRI of the ontology you would like to convert into the VOWL-JSON format):

java -jar owl2vowl.jar -iri "[Ontology IRI]"

For instance, the following command converts the FOAF vocabulary into the JSON file required for WebVOWL:

java -jar owl2vowl.jar -iri "http://xmlns.com/foaf/spec/"