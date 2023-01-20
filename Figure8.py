# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 03:19:01 2023

@author: darre
"""

import networkx as nx
import matplotlib.pyplot as plt

# Create a figure and axes object
fig, ax = plt.subplots()

# Create the graph H
H = nx.Graph()
H.add_nodes_from(["A", "B", "C", "D", "F", "T", "x", "y", "Community 1", "Self"])
H.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), 
                  ("F", "x"), ("x", "T"), ("T", "y"), ("A", "F"), ("D", "T"), 
                  ("F", "Community 1"), ("T", "Community 1"), ("Community 1", "Self")])
H.add_edges_from([("A", "B"),("D", "x")])
# Draw the graph
pos = nx.spring_layout(H)
nx.draw(H, pos, with_labels=True, ax = ax)
plt.show()


