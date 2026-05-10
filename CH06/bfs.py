rom typing import List, Dict, Optional
from collections import deque
from graph import Graph


def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.

    Returns:
        List of vertices forming the path, or None if no path exists
    """
    if start not in graph.vertices or end not in graph.vertices:
        return None

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.

    Returns:
        Dict mapping vertex -> distance from start
    """
    if start not in graph.vertices:
        return {}

    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    return bfs_find_path(graph, v1, v2) is not None
