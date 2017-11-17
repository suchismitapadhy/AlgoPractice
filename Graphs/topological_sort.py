from graph import Graph

visitedset = set()
topostack = []
def topologicalsort(g, visitedset, topostack):
    all_nodes = g.get_all_nodes()
    #do this while all nodes dont get added in visited
    while len(all_nodes) > 0:
        current_node = all_nodes.pop()
        if current_node not in visitedset:
            visitedset.add
            #explore children
            children = g.get_neighbors(current_node)
            for c in children:
                if c not in visitedset:
                    return topologicalsort(g, visitedset, topostack)



