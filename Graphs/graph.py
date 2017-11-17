class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, n1, n2, w=None):
        if n1 in self.adj_list:
            self.adj_list[n1][n2] = w
        else:
            self.adj_list[n1] = {n2: w}
        if n2 in self.adj_list:
            pass
        else:
            self.adj_list[n2] = {}

    def get_neighbors(self, n1):
        return self.adj_list[n1].keys()

    def get_all_nodes(self):
        return self.adj_list.keys()

    def get_edge_weights(self, n1, n2):
        return self.adj_list[n1][n2]

    def remove_edge(self, n1, n2):
        del self.adj_list[n1][n2]

    def add_node(self, n1):
        self.adj_list[n1] = {}


def main():
    g = Graph()
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('B', 'E')
    g.add_edge('D', 'F')
    g.add_edge('E', 'F')
    g.add_edge('F', 'G')
    print(g.get_all_nodes())
    print(g.get_neighbors('B'))
    g.add_node('X')
    print(g.get_all_nodes())


# main()


