def selection_sort(A):
    for idx in range(len(A)):
        #A[idx]=find min
        for j in range(idx,len(A)):
            if A[idx] > A[j]:
                A[idx], A[j] = A[j], A[idx]
    return A




alist = [5, 2, 91, 73, 23, 49, 101]
print(selection_sort(alist))