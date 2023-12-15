import networkx as nx

def read_graph_from_file(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue  # Skip header lines
            from_node, to_node = map(int, line.strip().split('\t'))
            G.add_edge(from_node, to_node)
    return G
