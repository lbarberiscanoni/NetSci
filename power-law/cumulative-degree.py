import scipy.io 
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw

sparse_mat = scipy.io.mmread('as-22july06.mtx')

G = nx.from_scipy_sparse_matrix(sparse_mat)

results = powerlaw.Fit(G)

powerlaw.plot_cdf(data=results)