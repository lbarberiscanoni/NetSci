import networkx as nx
import random

G = nx.Graph()

nodes = [x for x in range(10000)]
hubs = random.sample(nodes, 100)
edges = []
for node in nodes:
	edge = [node, random.choice(hubs)]
	edges.append(edge)

G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.write_gml(G, "gephi-graph.gml")

