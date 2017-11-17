def zero_matrix(arr):
    zero_i = set()
    zero_j = set()
    # find index(i,j) for zero valued elements
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                zero_i.add(i)
                zero_j.add(j)
    # traverse the matrix to set rows and cols to zero
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i in zero_i or j in zero_j:
                arr[i][j]=0
    return arr

print(zero_matrix([[1,2,3],[4,0,6],[7,8,9],[10,11,12]]))