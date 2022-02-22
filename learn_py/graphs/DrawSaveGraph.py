import networkx as x
import matplotlib.pyplot as plt
import scipy as sp
G = x.Graph()

vertices_list = [0,1,2,3,4,5,6,7]
G.add_nodes_from(vertices_list)
##print (G.nodes())
edges_list = [(0,1),(0,4),(0,7),(0,5),(1,7),(1,4),(1,3),(1,2),(2,3),(2,6),(3,4),(4,5),(4,7),(5,7)]
for edge in edges_list:
    G.add_edge(*edge)
A = x.adjacency_matrix(G)
##print (G.edges())


x.draw(G)   #rysowanie
plt.show()
m = A.todense()
print m
x.write_edgelist(G,'edgelist_save.py') #edge list save



