# implementation of an undirected graph using Adjacency Lists
class Vertex:
    def __init__(self, name):
        self.name=name
        self.neighbors=set()
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.add(v)
class Graph:
    def __init__(self):
        self.vertices = {}
    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        return False
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
                self.vertices[u].add_neighbor(v)
                self.vertices[v].add_neighbor(u)
                return True
        return False
    def print(self):
            for i in self.vertices:
                print(i,self.vertices[i].neighbors)

graph = Graph()
graph.addVertex(Vertex("A"))
graph.addVertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    graph.addVertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.addEdge(edge[:1], edge[1:])
graph.print()
