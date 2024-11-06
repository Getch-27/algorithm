from graphdataStructure import Graph

def dfs(graph, start_node, target_node):
    color, parent = {}, {}
    path_found = []

    # Initialize DFS properties for each node
    for node in graph.graph:
        color[node] = 'white'
        parent[node] = None

    # Helper function to perform DFS recursively
    def dfs_visit(current):
        color[current] = 'gray'
        path_found.append(current)
        
        # Check if we reached the target node
        if current == target_node:
            return True  # Target found, terminate the search

        # Traverse all adjacent nodes
        for neighbor in graph.graph[current]:
            if color[neighbor] == 'white':
                parent[neighbor] = current
                if dfs_visit(neighbor):  # Recursive call
                    return True  # Stop further calls if target is found

        color[current] = 'black'
        path_found.pop()  # Backtrack if no path found from this node
        return False

    # Start DFS from the start_node
    if dfs_visit(start_node):
        # Trace back the path from target to start using parent pointers
        path = []
        current = target_node
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()  # Reverse to get path from start to target
        print("Shortest Path in DFS: " + " --> ".join(path))
        return path
    else:
        print("Target node not reachable from start node.")
        return None

# Example usage
graph = Graph()
dfs(graph, "Miami", "San Francisco")
