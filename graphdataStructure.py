
class Graph:
    """
    A class to represent a graph data structure.

    Attributes
    graph : dict
        A dictionary to store the graph nodes and their connections.

    Methods
    __init__(self, textFile='cities.txt')
        Initializes the graph by parsing the given text file.

    add_edge(self, u, v)
        Adds a  edge between nodes u and v.

    display(self)
        Prints the graph nodes and their connections.

    parse_graph(self, textFile)
        Parses the given text file and populates the graph.
    """
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
# graph.display()