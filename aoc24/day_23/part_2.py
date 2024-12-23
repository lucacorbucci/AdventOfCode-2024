import networkx as nx
from networkx.algorithms import enumerate_all_cliques

def create_graph(connections):
    """
    Create a graph from the connections between the computers
    """
    G = nx.Graph()
    for connection in connections:
        G.add_edge(connection[0], connection[1])
    return G

connections = []
with open("input.txt") as file:
    for line in file:
        line = line.strip().split("-")
        connections.append((line[0], line[1]))

connection_graph = create_graph(connections)

# Find the largest clique in the graph and then get the names 
# of the nodes inside the clique and sort them.
all_cliques = max(enumerate_all_cliques(connection_graph), key=len)
password = ",".join(sorted([clique for clique in all_cliques]))
print(password)