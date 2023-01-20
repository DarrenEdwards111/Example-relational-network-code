import networkx as nx
import matplotlib.pyplot as plt

# Create the graph H
H = nx.Graph()
H.add_nodes_from(["A", "B", "C", "D", "F", "T", "x", "y", "Community 1", "Self"])
H.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("F", "x"), ("x", "T"), ("T", "y"), 
                  ("A", "F"), ("D", "T"), ("F", "Community 1"), 
                  ("T", "Community 1"), ("Community 1", "Self")])
H.add_edges_from([("A", "B"),("D", "x")])

# Draw the graph
pos = nx.spring_layout(H)
nx.draw_networkx_nodes(H, pos, node_size=200)
nx.draw_networkx_labels(H, pos, font_size=12)
nx.draw_networkx_edges(H, pos, alpha=0.5)

# Highlight the community "Community 1"
nodes_in_community_1 = [node for node in H.nodes() if node in ["F", "T", "x", "y"]]
nx.draw_networkx_nodes(H, pos, nodelist=nodes_in_community_1, node_color="red", node_size=200)

plt.show()
