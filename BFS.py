from graphdataStructure import Graph
from collections import deque

def bfs(graph, start_node):
    
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
        
        # Traverse all adjacent nodes
        for neighbor in graph.graph[current]:
            if color[neighbor] == 'white':  
                color[neighbor] = 'gray'
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)   

        color[current] = 'black'
    print(" --> ".join(node_order))

graph =Graph()
bfs(graph, "Seattle")
