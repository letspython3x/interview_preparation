class Graph:
    def __init__(self):
        self.data = {}
    
    def add_vertex(self, vertex):
        if vertex in self.data:
            raise RuntimeError(f"Vertex {vertex} already exists in graph.")
        self.data[vertex] = []
    
    def add_edge(self, v1, v2, weight):
        if v1 not in self.data:
            raise RuntimeError(f"vertext {v1} does not exists in graph.")
        elif v2 not in self.data:
            raise RuntimeError(f"vertext {v2} does not exists in graph.")
        
        self.data[v1].append((v2, weight))
    
    def get_adjancey_matrix(self):
        totalVertices = len(self.data)
        rows = [0 for count in range(totalVertices)]
        matrix = [rows.copy() for count in range(totalVertices)]
        for vertex, edge in self.data.items():  
            for col, weight in edge:
                matrix[vertex-1][col-1] = weight
        print(matrix)
        return matrix
    
    def traverse_graph(self):
        for vertex, edge in self.data.items():
            print("Vertex: ", vertex)
            print("Edges: ", edge)

def main():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1,2,12)
    graph.add_edge(1,3,13)
    graph.add_edge(2,3,23)
    graph.add_edge(2,4, 24)
    graph.add_edge(3,4, 34)
    graph.add_edge(4,1, 41)
    graph.traverse_graph()
    graph.get_adjancey_matrix()

if __name__ == "__main__":
    main()
    