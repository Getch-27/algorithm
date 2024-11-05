from graphdataStructure import Graph

def DFS(graph, start_node, target_node):
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
