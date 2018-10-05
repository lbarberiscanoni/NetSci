import scipy.io 
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw

sparse_mat = scipy.io.mmread('as-22july06.mtx')

G = nx.from_scipy_sparse_matrix(sparse_mat)

degree_sequence = sorted([y for x, y in G.degree()], reverse=True)

powerlaw.plot_cdf(degree_sequence)

# plt.show()
plt.savefig("cumulative-degree-distribution.png")