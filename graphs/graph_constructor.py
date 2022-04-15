"""Graph data structure
In a graph the edges (connections) can be weighted or non-weighted
They can be directional or by directional
We can show graphs with lists and matrixes
By directional graphs have a symmetrical matrix with a 0 diagonal
Trees and linked lists are some sort of graphs
    """


class Graph:
    """Create a graph data structure
    """

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        """This creates a vertex
        """
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        """Prints a graph
        """
        for key, value in self.adj_list.items():
            print(key, ':', value)

    def add_edge(self, vertex_1, vertex_2):
        """Add edges to a graph
        """
        if vertex_1 in self.adj_list.keys() and vertex_2 in self.adj_list.keys():
            self.adj_list[vertex_1].append(vertex_2)
            self.adj_list[vertex_2].append(vertex_1)
            return True
        return False

    def remove_edge(self, vertex_1, vertex_2):
        """Removes the edge between two vertexes
        """
        if vertex_1 in self.adj_list.keys() and vertex_2 in self.adj_list.keys():
            self.adj_list[vertex_1].remove(vertex_2)
            self.adj_list[vertex_2].remove(vertex_1)

    def remove_vertex(self, vertex):
        """This removes a vertex from a graph
        """
        if vertex in self.adj_list.keys():
            for item in self.adj_list[vertex]:
                self.adj_list[item].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


print("Let\'s create a graph with four vetexes")
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.print_graph()

print('Let\'s create an edge between these vertexes')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'D')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.print_graph()

print('Now let\'s remove the edge between A and B')
my_graph.remove_edge('A', 'B')
my_graph.print_graph()

print('Let\'s remove vertex A entirely')
my_graph.remove_vertex('A')
my_graph.print_graph()
