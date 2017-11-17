#Given A is N*N matrix
def matrix_rotation(A):
    new_matrix = [[None for _ in range(len(A[0]))] for _ in range(len(A))]
    n = len(A)-1
    for i in range(len(A)):
        for j in range(len(A[i])):
            new_matrix[j][n-i] = A[i][j]
    return new_matrix

def matrix_rotation_inplace(A):
    #step 1 --transpose
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    #step 2 -- reorder columns
    for i in range(len(A)):
        for j in range(len(A)//2):
            A[i][j],A[i][3-j] = A[i][3-j], A[i][j]
    return A




print(matrix_rotation_inplace([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))