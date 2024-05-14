from collections import deque
import heapq
from typing import Tuple, Union, List
import networkx as nx


def depth_first_search(graph, start, target, visited=None) -> bool:
    if visited is None:
        visited = set()
    visited.add(start)
    if start == target:
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, target, visited):
                return True
    return False


def breadth_first_search(graph, start, target) -> bool:
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False


def dijkstra(graph: nx.Graph, start: str, target: str, attribute: str) -> Tuple[Union[None, List[str]], Union[None, float]]:
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    queue = [(0, start)]

    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous.get(current_node)
            return path[::-1], distances[target]

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            distance = current_distance + graph[current_node][neighbor][attribute]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, None
