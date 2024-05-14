import networkx as nx
from task_1 import gen_ip_graph
from task_utils.algorithms import dijkstra


def main():
    graph = gen_ip_graph()

    for node in graph.nodes:
        for other_node in graph.nodes:
            if node == other_node:
                continue
            path, distance = dijkstra(graph, node, other_node, "latency")
            print(f"Shortest latency from {node} to {other_node}: {path}")
            print(f"Distance from {node} to {other_node}: {distance} ms")


if __name__ == "__main__":
    main()
