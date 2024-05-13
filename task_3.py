import networkx as nx
from task_1 import gen_ip_graph


def main():
    graph = gen_ip_graph()

    shortest_paths = dict(nx.all_pairs_dijkstra_path(graph, weight='latency'))

    # Print shortest paths between all pairs of nodes
    for source in shortest_paths:
        for target in shortest_paths[source]:
            if source != target:
                path = shortest_paths[source][target]
                path_length = nx.dijkstra_path_length(graph, source, target, weight='latency')
                print(f"Shortest path from {source} to {target}: {path} (length: {path_length} ms)")


if __name__ == "__main__":
    main()
