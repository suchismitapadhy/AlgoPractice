from graph import Graph

def bfs(G,S):
    visited = [] # order is important hence list
    queue = [S]
    while len(queue) > 0:
        # Removing that vertex from queue,whose neighbour will be visited now
        top = queue[0]
        queue = queue[1:]
        if top not in visited:
            visited.append(top)
            #// processing all the neighbours of top
            for c in G.get_neighbors(top):
                if c not in visited:
                    queue.append(c)
    return visited




def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(bfs(g,2))
    print(g.adj_list)
main()