from graphdataStructure import Graph
from collections import deque

def BFS(graph, start_node, target_node):
    color, distance, parent = {}, {}, {}
    
    for node in graph.graph:
        color[node] = 'white'
        distance[node] = float('inf')
        parent[node] = None

        
    node_order =[]
    color[start_node] = 'gray'
    distance[start_node] = 0
    queue = deque([start_node])
    
    print("Breadth-First Search Order:")
    
    # BFS Loop
    while queue:
        # Dequeue a node and process it
        current = queue.popleft()
        node_order.append(current)
        
        if current == target_node:
            # Trace back the path from target to start using parent pointers
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()  
            print("Shortest Path: " + " --> ".join(path))
            print("Traversal Order: " + " --> ".join(node_order)) 
            return path

        # Traverse all adjacent nodes
        for neighbor in graph.graph[current]:
            if color[neighbor] == 'white':  
                color[neighbor] = 'gray'
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)   

        color[current] = 'black'

    # If the target node is not reached
    print("Target node not reachable from start node.")
    print("Traversal Order: " + " --> ".join(node_order))  
    return None

# Example usage
graph = Graph()
BFS(graph, "Miami", "San Francisco")
