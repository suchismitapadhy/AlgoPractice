from graph import Graph

# given a master table (dictionary);
# amongst node that are not visited we have to pick the key with lowest value[0]
def find_min_value_key(table):
    min = float("inf")
    min_key = None
    for key in table:
        if table[key][1] == False: # table key value 1 stores if visited or not
            if table[key][0] < min: # table key value 2 stores the distance from source
                min = table[key][0]
                min_key = key
    return min_key

#Given: source Node, Graph
def djkstra(source, g):
    # construct the initial master table
    table = {}
    num_nodes = len(g.get_all_nodes())
    for n in g.get_all_nodes():
        table[n] =[float("inf"),False] # set all nodes to inf and visited as False
    # mark source distance = 0
    table[source][0] = 0 # set source node distance from source to 0
    curr = source
    for i in range(num_nodes-1):
        # find neighbors of current
        neighbors_of_current = g.get_neighbors(curr)
        # update weights of each neighbor
        for neighbor in neighbors_of_current:
            if table[neighbor][1]==True:
                pass
            else:
                new_dist = table[curr][0] + g.get_edge_weights(curr, neighbor)
                if new_dist < table[neighbor][0]:
                    table[neighbor][0] = new_dist
        # finished exploring the neighbors of curr --> updated all weights of neighbors
        # mark the current as visited
        table[curr][1] = True
        # pick new current --> pick amongst the lowest unvisited
        curr = find_min_value_key(table)
    return table

def main():
    g = Graph()
    g.add_edge(1, 6, 14)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 2, 7)
    g.add_edge(2, 1, 7)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 1, 9)
    g.add_edge(3, 2, 10)
    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 2, 15)
    g.add_edge(4, 3, 11)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 4, 6)
    g.add_edge(5, 6, 9)
    g.add_edge(6, 1, 14)
    g.add_edge(6, 3, 2)
    g.add_edge(6, 5, 9)

    # print(g.get_neighbors(1))

    print(djkstra(1, g))
if __name__=="__main__":
    main()




