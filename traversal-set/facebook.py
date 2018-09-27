import networkx as nx
from pprint import pprint

fbGraph = nx.read_edgelist("facebook_combined.txt")

#get all shortest paths
shortestPaths_raw = nx.shortest_path(fbGraph)

#all shortest paths
#pprint(shortestPaths_raw)
#print(shortestPaths_raw)

#select i, j
i = "414"
j = "567"

#extract shortest paths from the i, j dictionary
shortestPaths_full = []
for val in shortestPaths_raw:
	for path in shortestPaths_raw[val]:
		shortestPath = shortestPaths_raw[val][path]
		shortestPaths_full.append(shortestPath)

#only get shortest paths with i and j in them
traversalSet = [path for path in shortestPaths_full if (i in path and j in path)]

#narrow it to shortest paths where i and j are connected through just 1 edge
traversalSet_noDuplicates = []
for path in traversalSet:
	subL = [ [ path[i], path[i +1] ] for i in range(len(path) - 1) ]
	if [i, j] in subL:
		traversalSet_noDuplicates.append(path)

# for path in traversalSet_noDuplicates:
# 	print(path)

#compute the traversal set 
print(len(traversalSet_noDuplicates))


#count the # of paths after you remove duplicates based on the endpoint (remember to check for inverses)
#

