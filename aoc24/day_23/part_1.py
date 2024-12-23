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
# Enumerate all the cliques of size 3 in the graph. A clique is a complete subgraph
# of the graph where all nodes are connected to all other nodes.
all_cliques = filter(lambda x: len(x) == 3, enumerate_all_cliques(connection_graph))
all_cliques = set([tuple(clique) for clique in list(all_cliques) for node in clique if node[0] == "t"])

print(len(all_cliques))