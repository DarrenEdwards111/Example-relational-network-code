# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 07:26:45 2023

@author: darre
"""
import community
import networkx as nx
import matplotlib.pyplot as plt

# Create a figure and axes object
fig, ax = plt.subplots()

# Create the graph H
H = nx.Graph()
H.add_nodes_from(["A", "B", "C", "D", "F", "T", "x", "y"])
H.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("F", "x"), ("x", "T"), ("T", "y"), ("A", "F"), ("D", "T")])
H.add_edge("C", "A")
H.add_edge("A", "D")
H.add_edge("C", "A")

# Use the Louvain algorithm to detect communities in H
partition = community.best_partition(H)

# Get the sizes of the communities
sizes = [len([v for v in partition.values() if v == i]) for i in set(partition.values())]

# Plot the graph with different colors for each community
pos = nx.spring_layout(H)
for i, com in enumerate(set(partition.values())):
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
    nx.draw_networkx_nodes(H, pos, list_nodes, node_size = 20, node_color = str(i/len(set(partition.values()))))
    nx.draw_networkx_edges(H, pos, alpha=0.5)

plt.show()
