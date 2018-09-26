import networkx as nx

fbGraph = nx.read_edgelist("facebook_combined.txt")

shortestPath = nx.shortest_path(fbGraph)


print(shortestPath["3372"]["192"])

#lapMat = nx.laplacian_matrix(fbGraph)

#print(lapMat)

eigenCentrality = nx.eigenvector_centrality_numpy(fbGraph)

sortedEigens = sorted(eigenCentrality.items(), key=lambda x: x[1])

print(sortedEigens[0:4])