def insertionSort(A):
    for index in range(1, len(A)):
        currentValue = A[index]
        i = index - 1
        while i >= 0:
            if currentValue < A[i]:
                # A[i] moved right one place
                A[i + 1] = A[i]
                A[i] = currentValue
                i -= 1
            else:
                break
    return A


alist = [5, 2, 91, 73, 23, 49, 101]
print(insertionSort(alist))
