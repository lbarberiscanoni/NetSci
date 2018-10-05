import scipy.io 
import networkx as nx
import matplotlib.pyplot as plt
import collections 

sparse_mat = scipy.io.mmread('as-22july06.mtx')

G = nx.from_scipy_sparse_matrix(sparse_mat)

degree_sequence = sorted([y for x, y in G.degree()], reverse=True)

raw_sequence = collections.Counter(degree_sequence)

degrees = []
counts = []

for x, y in sorted(raw_sequence.items()):
	degrees.append(x)
	counts.append(y)

print(max(degrees))
print(max(counts))

plt.bar(degrees, counts)

# plt.show()
plt.savefig("degree_histogram.png")