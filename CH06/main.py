from graph import create_texas_road_network
from bfs import bfs_find_path, bfs_all_reachable


def main():
    print("=" * 60)
    print("PART 1: TEXAS ROAD NETWORK GRAPH")
    print("=" * 60)

    roads = create_texas_road_network()
    print(f"\nCreated graph with {len(roads)} cities")
    roads.display()

    print("\n" + "=" * 60)
    print("PART 2: SHORTEST PATH (BFS)")
    print("=" * 60)

    path = bfs_find_path(roads, "Houston", "El Paso")
    if path:
        print(f"\nRoute: {' → '.join(path)}")

    print("\n" + "-" * 40)
    path = bfs_find_path(roads, "Houston", "McKinney")
    if path:
        print(f"\nRoute: {' → '.join(path)}")

    print("\n" + "=" * 60)
    print("PART 3: DISTANCES FROM HOUSTON")
    print("=" * 60)

    distances = bfs_all_reachable(roads, "Houston")

    print("\nCities by distance (edges) from Houston:")
    for dist in range(max(distances.values()) + 1):
        cities_at_dist = [c for c, d in distances.items() if d == dist]
        if cities_at_dist:
            print(f"  {dist} edge(s): {', '.join(sorted(cities_at_dist))}")
