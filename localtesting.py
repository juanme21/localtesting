from rdflib import Graph, BNode, Literal, URIRef

g = Graph()
g.parse("./pizza.owl")
print(len(g))
metrics = {"classes": 0, "": 0}
un = 0
for s, p, o in g:
    if str(o) == "http://www.w3.org/2002/07/owl#Class":
        # print(o)
        un += 1
    if str(o) == "http://www.w3.org/2002/07/owl#ObjectProperty":
        # print(o)
        un += 1

    if str(o) == "http://www.w3.org/2002/07/owl#DataProperty":
        # print(o)
        un += 1

    if str(o) == "http://www.w3.org/2002/07/owl#NamedIndividual":
        # print(o)
        un += 1

    if str(o) == "http://www.w3.org/2002/07/owl#AnnotationProperty":
        print(o)
        un += 1

    if str(p) == "http://www.w3.org/2000/01/rdf-schema#subClassOf":
        # print(p)
        un += 1
