# -*- coding: UTF-8 -*-
import networkx as nx
import os

gmlPath = 'gmls\\Mod_0 It_2.gml'

def clearGml(gmlPath):
	G = nx.read_gml(gmlPath)
	nodos = dict(G.nodes())

	for n in nodos:
		if('hIndex' in nodos[n]):
			pass
			# nodos[n]['numCoAuthors'] = sum(1 for _ in G.neighbors(n))
			# print(nodos[n]['numCoAuthors'])

	for n in nodos:
		if('hIndex' not in nodos[n]):
			G.remove_node(n)

	nx.write_gml(G, 'clearG' + gmlPath[1:])

for folder in os.listdir('gmls'):
	print(os.path.join('gmls\\', folder))
	clearGml(os.path.join('gmls\\', folder))

