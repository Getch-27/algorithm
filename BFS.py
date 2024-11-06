from graphdataStructure import Graph
from collections import deque

def BFS(graph, start_node, target_node):
    """
    Performs a Breadth-First Search (BFS) on a graph to find the shortest path from a start node 
    to a target node.

    This function explores all the nodes in the graph level by level, starting from the `start_node`. 
    It maintains a queue to keep track of the nodes to be explored and a distance map to store the 
    distance from the start node to each node. If the target node is found, it traces back the path 
    from the target node to the start node using parent pointers and prints the shortest path and traversal order.
    
    Parameters:
        graph (Graph): An instance of the `Graph` class containing the graph data structure.
        start_node (str): The starting node for the BFS traversal.
        target_node (str): The target node to be found during the traversal.
    
    Returns:
        list: A list representing the shortest path from `start_node` to `target_node` if reachable, 
              otherwise `None`.
    
    Example:
        graph = Graph()
        BFS(graph, "Miami", "San Francisco")
    
    Output:
        If the target node is reachable from the start node:
        - Prints the shortest path found from start to target node.
        - Prints the order in which nodes were visited during the BFS traversal.
    
        If the target node is not reachable:
        - Prints a message indicating that the target node is not reachable.
        - Prints the order in which nodes were visited during the BFS traversal.
    
    Time Complexity:
        - The BFS algorithm visits every node and edge in the graph. Thus, the time complexity is O(V + E),
          where V is the number of vertices (nodes) and E is the number of edges in the graph.
    
    Space Complexity:
        - The space complexity is O(V), as we store color, distance, parent, and the queue, all of which 
          depend on the number of nodes in the graph.
    """
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
