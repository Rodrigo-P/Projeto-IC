import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])


G.add_edge(1,2)
G.add_edges_from([(1,2),(3,1)])

G.number_of_nodes()
G.number_of_edges()


G[1][2]['weight']= 1
G.add_edge(3,2,weight=0.4)
for (u,v,wt) in G.edges.data('weight'):
	if wt>0.5:
		print('(%d,%d,%f)'%(u,v,wt))


DG = nx.DiGraph()

DG.add_weighted_edges_from([(1,2,0.5),(3,1,0.625)])
print(list(DG.successors(1)))
print(list(DG.predecessors(1)))

H = nx.Graph(DG)

plt.subplot(122)
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show(122)