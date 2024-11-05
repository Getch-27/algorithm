from graphdataStructure import Graph

def dfs(graph, start_node):
    
    color, parent = {}, {}
    node_order = []
    
    for node in graph.graph:
        color[node] = 'white'
        parent[node] = None

    def dfs_visit(node):
        color[node] = 'gray'
        node_order.append(node)
        
        # Traverse all adjacent nodes
        for neighbor in graph.graph[node]:
            if color[neighbor] == 'white':
                parent[neighbor] = node
                dfs_visit(neighbor)

        color[node] = 'black'

    print("Depth-First Search Order:")
    dfs_visit(start_node)
    print(" --> ".join(node_order))

graph = Graph()
dfs(graph, "Seattle")
