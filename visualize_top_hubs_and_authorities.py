import networkx as nx
import matplotlib.pyplot as plt

def visualize_hubs_and_authorities(input_graph):
    # The HITS algorithm computes two numbers for a node. Authorities estimates the node value based on the incoming links.
    # Hubs estimates the node value based on outgoing links
    hubs, authorities = nx.hits(input_graph)

    # Normalize the scores for visualization purposes
    max_hub_score = max(hubs.values())
    max_authority_score = max(authorities.values())
    hubs = {node: score / max_hub_score * 500 for node, score in hubs.items()}  # scaling to 500 for node size
    authorities = {node: score / max_authority_score * 500 for node, score in authorities.items()}  # scaling to 500 for node size

    # Positioning for nodes in the graph
    pos_subgrafo = nx.spring_layout(input_graph)

    # Plot the graph
    plt.figure(figsize=(10, 8))

    # Draw hubs in red
    nx.draw_networkx_nodes(input_graph, pos_subgrafo, nodelist=hubs.keys(), node_size=[hubs[node] for node in input_graph], node_color='red')

    # Draw authorities in blue
    nx.draw_networkx_nodes(input_graph, pos_subgrafo, nodelist=authorities.keys(), node_size=[authorities[node] for node in input_graph], node_color='blue')

    # Draw all edges
    nx.draw_networkx_edges(input_graph, pos_subgrafo)

    # Draw labels
    nx.draw_networkx_labels(input_graph, pos_subgrafo, font_weight='bold')

    plt.title(f'Stanford pages with Hubs and Authorities Highlighted')
    plt.show()
