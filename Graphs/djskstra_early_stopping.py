from graph import Graph

# given a master table (dictionary);
# amongst node that are not visited we have to pick the key with lowest value[0]
def find_min_value_key(table):
    min = float("inf")
    min_key = None
    for key in table:
        if table[key][1] == False:
            if table[key][0] < min:
                min = table[key][0]
                min_key = key
    return min_key

#Given: source Node, Graph
def djkstra(source, destination, g):
    # construct the initial master table
    table = {}
    num_nodes = len(g.get_all_nodes())
    for n in g.get_all_nodes():
        table[n] =[float("inf"),False, None]
    # mark source distance = 0
    table[source][0] = 0
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
                    table[neighbor][2] = curr
        # finished exploring the neighbors of curr --> updated all weights of neighbors
        # mark the current as visited
        table[curr][1] = True
        # pick new current --> pick amongst the lowest unvisited
        curr = find_min_value_key(table)
        # early stopping
        # when the destination node is marked visited --> our job is done--> we can return the table
        if curr == destination:
            return table
    return table

def find_path(source, destination, g):
    path = str(destination)
    master_table = djkstra(source, destination, g)
    print(master_table)
    current = destination
    while current is not None:
        path = str(master_table[current][2])+"-->" + path
        current = master_table[current][2]
    return path

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

    #print(djkstra(1, g))

    print(find_path(1,6, g))

if __name__=="__main__":
    main()




