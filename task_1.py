import networkx as nx
import random


def gen_ip_graph() -> nx.Graph:
    random.seed(42)
    graph = nx.Graph()

    graph.add_node("Main Router", ip="192.168.0.1")

    for i in range(3):
        graph.add_node(f"Router {i + 1}", ip=f"192.168.0.{i + 2}")

    for i in range(9):
        graph.add_node(f"User {i + 1}", ip=f"192.168.0.{i + 18}")

    graph.add_edges_from([("Main Router", f"Router {i + 1}") for i in range(3)], latency=random.randint(20, 40))

    for i in range(0, 3):
        for j in range(0 + i * 3, 3 + i * 3):
            graph.add_edges_from([(f"Router {i + 1}", f"User {j + 1}")], latency=random.randint(50, 100))

    graph.add_edges_from([("Main Router", f"User {10}", {'ip': '192.168.0.18', 'latency': random.randint(1, 100)}),
                          ("Main Router", f"User {11}", {'ip': '192.168.0.19', 'latency': random.randint(1, 100)})
                          ])

    return graph


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd

    G = gen_ip_graph()
    nodes = [node for node in G.nodes]
    graph_data = pd.DataFrame(columns=nodes, index=["Degree Centrality", "Closeness Centrality", "Betweenness Centrality"])
    nodes_data = {node: round(nx.degree_centrality(G)[node], 3) for node in nodes}
    graph_data.loc["Degree Centrality"] = [nodes_data[node] for node in nodes]
    nodes_data = {node: round(nx.closeness_centrality(G)[node], 3) for node in nodes}
    graph_data.loc["Closeness Centrality"] = [nodes_data[node] for node in nodes]
    nodes_data = {node: round(nx.betweenness_centrality(G)[node], 3) for node in nodes}
    graph_data.loc["Betweenness Centrality"] = [nodes_data[node] for node in nodes]
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)

    # print(nx.to_dict_of_lists(G))

    fig, axs = plt.subplots(2, 1, figsize=(12, 12))

    options = {
        'node_color': 'lightblue',
        'node_size': 1000,
        'with_labels': True,
        'font_size': 10,
        'font_color': 'black',
        'font_weight': 'bold',
        'edge_color': 'gray',
        'width': 2,
    }

    nx.draw(G, pos=nx.spring_layout(G, seed=42), ax=axs[0], **options)
    edge_labels = {(u, v): f"{data['latency']} ms" for u, v, data in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G, seed=42), edge_labels=edge_labels, ax=axs[0])

    axs[0].set_title('Graph Visualization', fontsize=16, fontstyle="italic")

    info_text = f"Number of Nodes: {num_nodes}\nNumber of Edges: {num_edges}\nConnected: {is_connected}"
    axs[1].text(0.5, 0.5, info_text, transform=axs[1].transAxes, ha="center", va="center", fontsize=12)
    table = axs[1].table(cellText=graph_data.values, colLabels=graph_data.columns, rowLabels=graph_data.index,
                         loc="bottom", cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    axs[1].axis('off')  # Hide axis for the info subplot
    axs[1].set_title('Graph Information', fontsize=16, fontstyle="italic")

    plt.tight_layout()
    plt.show()
