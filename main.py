import sys
from read_graph import read_graph_from_file
from visualize_top_hubs_and_authorities import visualize_hubs_and_authorities

if __name__ == "__main__":
    graph_file_path = sys.argv[1];
    graph = read_graph_from_file(graph_file_path)
    visualize_hubs_and_authorities(graph)