import sys
from read_graph import read_graph_from_file

if __name__ == "__main__":
    graph_file_path = sys.argv[1];
    graph = read_graph_from_file(graph_file_path)
    print(f"Number of nodes: {graph.number_of_nodes()}")
    print(f"Number of edges: {graph.number_of_edges()}")