from pyvis.network import Network
import pandas as pd
import networkx as nx
df = pd.read_excel('mbti_vers2.xlsx')
net = Network()
nodes = list(set(df["mbti"]).union(df["actor"]))
vertex1 = df['mbti'].to_list()
vertex2 = df['actor'].to_list()
edges = [list(l) for l in zip(vertex1,vertex2)]
net.add_nodes(nodes)
net.add_edges(edges)
net.show_buttons(filter_=['nodes', 'edges', 'physics'])
net.show("character3.html")
