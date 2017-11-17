from graph import Graph

def detect_cycle(g):
    white = set(g.get_all_nodes())
    gray = set()
    black = set()

    while len(white)>0:
        start = white.pop()
        if dfs(g,start,white,gray,black):
            return True
    return False

def dfs(g,current,white,gray,black):
    gray.add(current)
    children = g.get_neighbors(current)
    for child in children:
        if child in black:
            #We are safe... don't do anything and look at the next child
            continue
        if child in gray:
            # Bingo we got a cycle
            return True
        if child in white:
            # It's a new node. remove it from white and run dfs on it
            white.remove(child)
            if dfs(g,child,white,gray,black):
                return True
    gray.remove(current)
    black.add(current)
    return False




g = Graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1, 3)
g.add_edge(4, 1)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)

if detect_cycle(g):
    print("Contains Cycle")
else:
    print("No cycles")





