from graph import Graph

def dfs(G, S):
    visited = []
    stack = [S]
    while len(stack) > 0:
        top = stack[0]
        stack = stack[1:]
        if top not in visited:
            visited.append(top)
            for c in G.get_neighbors(top):
                if c not in visited:
                    stack.insert(0,c)
    return visited

#################################################

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
    g.add_edge(6, 7)
    g.add_edge(6, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)


    print(dfs(g, 2))
    print(g.adj_list)

main()