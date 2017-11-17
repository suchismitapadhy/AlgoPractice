#Given A is M*N matrix
def zerofy(A):
    numrows = len(A)
    numcols = len(A[0])
    row = set()
    col = set()
    for i in range(numrows):
        for j in range(numcols):
            if A[i][j]==0:
                row.add(i)
                col.add(j)

    for i in range(numrows):
        for j in range(numcols):
            if i in row or j in col:
                A[i][j]=0
    return A

def print_matrix(A):
    numrows = len(A)
    numcols = len(A[0])
    for i in range(numrows):
        for j in range(numcols):
            print(A[i][j],end="\t")
        print()

print_matrix(zerofy([[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))