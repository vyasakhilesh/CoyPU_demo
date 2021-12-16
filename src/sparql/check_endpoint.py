from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://localhost:7200/repositories/coypu_demo")
# http://coypu_demo_graphdb:7200/repositories/coypu_demo
# sparql = SPARQLWrapper("http://dbpedia.org/sparql/")
sparql.setQuery(
    """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <https://data.coypu.org/countries/AFG> rdfs:label ?label } limit 10
"""
)
sparql.setReturnFormat(JSON)
print(sparql.query())
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["label"]["value"])

print("---------------------------")

for result in results["results"]["bindings"]:
    print("%s: %s" % (result["label"]["xml:lang"], result["label"]["value"]))
