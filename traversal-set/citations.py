import networkx as nx
from pprint import pprint
import itertools

citGraph = nx.read_edgelist("cit-HepTh.txt")

#get all shortest paths
shortestPaths_raw = nx.shortest_path(citGraph)

#all shortest paths
#pprint(shortestPaths_raw)
#print(shortestPaths_raw)

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
		endpoints = [path[0], path[len(subL)]]
		# print(path, subL, endpoints)
		shortestPaths_narrow.append(endpoints)

# for path in shortestPaths_narrow:
# 	print(path)


#compute the traversal set by removing duplicates 
shortestPaths_narrow.sort()
traversalSet = list(x for x,_ in itertools.groupby(shortestPaths_narrow))

print(traversalSet)
print(len(traversalSet))