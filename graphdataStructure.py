class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def display(self):
        for node, neighbors in self.graph.items():
            print(f"Node {node} is connected to: {', '.join(map(str, neighbors))}")

def parse_graph(textFile):
    graph = Graph()
    with open (textFile, 'r') as file:
        for line in file:
            source, destination = line.strip().split(',')
            graph.add_edge(source, destination)
    return graph
        
graph = parse_graph('cities.txt')
graph.display()


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.display()