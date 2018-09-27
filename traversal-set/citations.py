import networkx as nx
from pprint import pprint

citGraph = nx.read_edgelist("cit-HepTh.txt")

shortestPaths_raw = nx.shortest_path(citGraph)

#all shortest paths
#pprint(shortestPaths_raw)
#print(shortestPaths_raw)

i = "9302103"
j = "1103"

shortestPaths_full = []
for val in shortestPaths_raw:
	for path in shortestPaths_raw[val]:
		shortestPath = shortestPaths_raw[val][path]
		shortestPaths_full.append(shortestPath)

traversalSet = [path for path in shortestPaths_full if (i in path and j in path)]
for path in traversalSet:
	print(path)



