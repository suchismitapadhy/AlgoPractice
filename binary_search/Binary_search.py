def binary_search(A, item, start, end):
    while start <= end:
        mid = (start+end)/2
        if item==mid:
            return mid
        elif item < mid:
            end = mid-1
        else:
            #item > mid:
            start = mid+1
    return -1

A = [2,7,10,33,78,91,100]
print(binary_search(A,91,0,6))
