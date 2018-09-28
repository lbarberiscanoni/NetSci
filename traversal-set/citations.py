import networkx as nx
from pprint import pprint
import itertools

citGraph = nx.read_edgelist("cit-HepTh.txt")

#get all shortest paths
shortestPaths_raw = nx.shortest_path(citGraph)

#select i, j
i = "9302103"
j = "1103"

#extract shortest paths from the i, j dictionary
shortestPaths_full = []
for val in shortestPaths_raw:
	for path in shortestPaths_raw[val]:
		shortestPath = shortestPaths_raw[val][path]
		shortestPaths_full.append(shortestPath)

#only get shortest paths with i and j in them
shortestPaths_relevant = [path for path in shortestPaths_full if (i in path and j in path)]

#narrow it to shortest paths where i and j are connected through just 1 edge
shortestPaths_narrow = []
for path in shortestPaths_relevant:
	subL = [ [ path[i], path[i +1] ] for i in range(len(path) - 1) ]

	if [i, j] in subL:
		endpoints = [path[0], path[len(path) - 1]]
		#print(path, subL, endpoints)
		shortestPaths_narrow.append(endpoints)


#compute the traversal set by removing duplicates explicitly
shortestPaths_narrow.sort()
traversalSet = list(x for x,_ in itertools.groupby(shortestPaths_narrow))

print("# of keys in the shortest path dictionary", len(shortestPaths_raw))
print("# of all shortest paths", len(shortestPaths_full))
print("# of shortests paths that include (i, j)", len(shortestPaths_relevant))
print("# of shortest paths that include i and j connected through 1 edge", len(shortestPaths_narrow))
print("traversal set centrality", len(traversalSet))