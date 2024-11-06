from graphdataStructure import Graph

def DFS(graph, start_node, target_node):
    """
    Performs a Depth-First Search (DFS) on a graph to find the path from a start node to a target node.
    
    This function traverses the graph starting from the `start_node` and explores as far as possible along 
    each branch before backtracking. If the target node is found, it traces back the path from the target 
    to the start node using parent pointers and prints the path and traversal order.
    
    parameters:
        graph (Graph): An instance of the `Graph` class containing the graph data structure.
        start_node (str): The starting node for the DFS traversal.
        target_node (str): The target node to be found during the traversal.
    
    Returns:
        list: A list representing the path from `start_node` to `target_node` if reachable, otherwise `None`.
    
    Example:
        graph = Graph()
        DFS(graph, "Miami", "San Francisco")
    
    Output:
        If the target node is reachable from the start node:
        - Prints the path found from start to target node.
        - Prints the order in which nodes were visited during the DFS traversal.
    
        If the target node is not reachable:
        - Prints a message indicating that the target node is not reachable.
        - Prints the order in which nodes were visited during the DFS traversal.
    
    Time Complexity:
        - In the worst case, DFS will visit all nodes and edges, making the time complexity O(V + E),
          where V is the number of vertices (nodes) and E is the number of edges in the graph.
    
    Space Complexity:
        - The space complexity is O(V), as we store color, parent, node_order, and path, all of which 
          depend on the number of nodes in the graph.
    """
    color, parent = {}, {}
    
    for node in graph.graph:
        color[node] = 'white'
        parent[node] = None

    node_order = []
    path = []

    def dfs_visit(node):
        nonlocal path
        color[node] = 'gray'
        node_order.append(node)
        
        if node == target_node:
            # Trace back the path from target to start using parent pointers
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()  
            print("Path Found: " + " --> ".join(path))
            print("Traversal Order: " + " --> ".join(node_order))  # Print traversal order
            return True

        for neighbor in graph.graph[node]:
            if color[neighbor] == 'white':
                parent[neighbor] = node
                if dfs_visit(neighbor):  # Recur for DFS
                    return True  
        
        color[node] = 'black'
        return False

    print("Depth-First Search Order:")
    if dfs_visit(start_node):
        return path
    else:
        print("Target node not reachable from start node.")
        print("Traversal Order: " + " --> ".join(node_order)) 
        return None


graph = Graph()
DFS(graph, "Miami", "San Francisco")
