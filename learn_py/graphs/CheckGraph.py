import networkx as x
G = x.Graph()
"""Dane w kodzie programu, bez generatora"""
## example in repository
vertices_list = [0,1,2,3,4,5,6,7]
edges_list = [(0,1),(0,4),(0,7),(0,5),(1,7),(1,4),(1,3),(1,2),(2,3),(2,6),(3,4),(4,5),(4,7),(5,7)]

##full graph, tree, bipartite example
##vertices_list = [0,1]
##edges_list = [(0,1)]

##full graph, cycle example
##vertices_list = [0,1,2]
##edges_list = [(0,1),(1,2),(2,0)]







G.add_nodes_from(vertices_list)
for edge in edges_list:
    G.add_edge(*edge)

#tree
print 'Is tree :', x.is_tree(G)
#bipartite
print 'Is bipartite :',x.is_bipartite(G)
#cycle
if x.cycle_basis(G):
    cycle_list = x.cycle_basis(G)
    print cycle_list
    if len(vertices_list) == len(cycle_list[0]):
        is_cycle = True
    else:
        is_cycle = False
else:
    is_cycle = False
print 'Is cycle :', is_cycle
#full graph
n = len(vertices_list)
for node in vertices_list:
    if G.degree(node)==(n-1):
        full_graph = True
    else:
        full_graph = False
        break
print'Is full :', full_graph

##full graph example
