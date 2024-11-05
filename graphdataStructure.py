class Graph:
    def __init__(self, textFile='cities.txt'):
        self.graph = {}
        self.parse_graph(textFile)

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

    def parse_graph(self, textFile):
        try:
            with open(textFile, 'r') as file:
                for line in file:
                    source, destination = line.strip().split(',')
                    self.add_edge(source, destination)
        except FileNotFoundError:
            print(f"Error: File '{textFile}' not found.")
    
    

   
# graph = parse_graph('cities.txt')
# graph.visualize()


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.display()