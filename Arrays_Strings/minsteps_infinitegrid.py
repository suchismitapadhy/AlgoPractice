    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
def coverPoints(X, Y):
    dist = 0
    for i in range(len(X) - 1):
        dist += distance(X[i], Y[i], X[i + 1], Y[i + 1])
    return dist


def distance(X1, Y1, X2, Y2):
    #  maximum of abs(x2-x1) and abs(y2-y1).
    return max(abs(X1 - X2), abs(Y1 - Y2))

# Input : [(0, 0), (1, 1), (1, 2)]
# Output : 2

X = [0,1,1]
Y= [0,1,3]

print(coverPoints(X,Y))

# #Algo:
#     As we have to cover all the given points in the specified order,
#     if we can find the minimum number of steps required to reach from a starting point
#     to next point, the sum of all such minimum steps for covering all the points would
#     be our answer.

#     One way to reach form a point (x1,y1) to (x2, y2) is to move abs(x2-x1) steps
#     in horizontal direction and abs(y2-y1) steps in vertical direction,
#     but this is not the shortest path to reach (x2,y2). The best way would be to cover
#     the maximum possible distance in diagonal direction and remaining in horizontal
#     or vertical direction. If we look closely this just reduces to maximum
#     of abs(x2-x1) and abs(y2-y1).

