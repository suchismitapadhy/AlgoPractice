def rotate_perpendicular(arr):
    new_arr = [[0 for i in j] for j in arr]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
             new_arr[j][len(arr)-i-1] = arr[i][j]
    return new_arr
print(rotate_perpendicular([[1,2,3],[4,5,6],[7,8,9]]))