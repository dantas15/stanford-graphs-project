import networkx as nx

def print_top_hubs_and_authorities(graph, n=5):
  hubs, authorities = nx.hits(graph, max_iter=100, tol=1e-08, nstart=None, normalized=True)
  top_hubs = sorted(hubs.items(), key=lambda x: x[1], reverse=True)[:n]
  top_authorities = sorted(authorities.items(), key=lambda x: x[1], reverse=True)[:n]

  print("Top Hubs:")
  for node, score in top_hubs:
      print(f"Node {node}: {score}")

  print("\nTop Authorities:")
  for node, score in top_authorities:
      print(f"Node {node}: {score}")