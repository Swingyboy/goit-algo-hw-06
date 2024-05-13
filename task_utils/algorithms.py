from collections import deque


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
