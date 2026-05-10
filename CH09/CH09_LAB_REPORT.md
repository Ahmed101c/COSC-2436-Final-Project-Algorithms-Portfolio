Student Information

Name: Ahmed Ajlal
Date: 04/11/2026
Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build?
 Undirected, weighted graph.

Why must all edge weights be non-negative for Dijkstra's to work?
Dijkstra’s algorithm assumes that once the smallest-cost unvisited node is chosen, its shortest path is final. This only remains true when all edge weights are non-negative. If a negative edge exists, a shorter path to an already processed node could appear later, which would make the algorithm give the wrong answer. 

Time Complexity (with simple array scan for min-node):
 O(V²)

Time Complexity (with a min-heap/priority queue): 
O((V + E) log V)

Core Data Structures

Structure	Variable Name	What It Stores
Adjacency dict	graph	  Each node’s neighbors and
                       the weight of each edge
Cost table	costs	Current shortest known distance from the start node to each node
Parent table	parents	  Previous node on the shortest known path
Visited list	processed	Nodes whose shortest distance has been finalized
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:
Edges:
A-B(1), A-C(4), B-C(2), B-D(6), C-D(3)
Start at A 
nitial values:
costs[A] = 0
costs[B] = 1
costs[C] = 4
costs[D] = ∞

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	—					
1						
2						
3						
4						
Shortest path A to D: A → B → C → D
Total cost: 6

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?
Infinity represents unknown/unreachable distances at the start. The start node is 0 because its distance to itself is zero.

Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?
It represents an undirected graph where travel works both ways. If only one direction is stored, some valid paths become unreachable.

The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?
A min-heap quickly retrieves the smallest-cost node. This reduces time from O(V²) to about O((V + E) log V), which is much faster for large graphs.

If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?
A negative edge can create a cheaper path after a node is finalized, breaking Dijkstra’s assumption. The Bellman–Ford algorithm correctly handles negative weights.

How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?
Each node stores the previous node on the shortest path. Tracing backward builds the path from destination to source, so it must be reversed.

What happens when the source and destination are in disconnected components of the graph? How does the code detect this?
The destination’s cost remains infinity, meaning no path exists. The algorithm detects this because the node’s cost never updates.
