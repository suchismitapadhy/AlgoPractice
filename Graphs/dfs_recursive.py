from graph import Graph

def dfs_util(g, node, visitedset):
    print(node)
    visitedset.add(node)
    for c in g.get_neighbors(node):
        if c not in visitedset:
            dfs_util(g, c, visitedset)


def dfs(g):
    visitedset = set()
    all_nodes = g.get_all_nodes()
    for node in all_nodes:
        if node not in visitedset:
            dfs_util(g, node, visitedset)
            print("ok done")


def main():
    g = Graph()
    g.add_edge(0, 2)
    g.add_edge(0, 4)
    g.add_edge(1, 5)
    g.add_edge(1, 3)
    g.add_edge(2, 1)
    g.add_edge(2, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 0)
    g.add_edge(4, 2)
    g.add_edge(4, 6)
    g.add_edge(6, 2)
    g.add_edge(6, 5)
    g.add_edge(5, 6)


    dfs(g)
main()
