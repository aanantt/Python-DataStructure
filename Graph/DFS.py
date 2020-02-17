class Vertex:
    def __init__(self, n):
        self.name=n
        self.isVisited=False
        self.neighbors=list()
    def add_neighbor(self, v):
        nset=set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()
class Graph:
    def __init__(self):
        self.vertices = {}
    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex] = vertex
            return True
        return False

    def addEdge(self, u, v):
        u=Vertex(u)
        v=Vertex(v)
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False
    def _DFS(self):
        for x in self.vertices:
            if x.isVisited == False:
                self.DFS(x)
    def DFS(self,node):
        for i in self.vertices[node].neighbors:
            if i.isVisited == False:
               self.DFS(i)
        node.isVisited = True
        print(node.name)
graph = Graph()
for i in range(ord('A'), ord('K')):
    graph.addVertex(Vertex(chr(i)))
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.addEdge(edge[:1], edge[1:])
graph._DFS()
