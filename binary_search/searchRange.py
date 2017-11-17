def searchRange(A, B):
    start = 0
    end = len(A) - 1
    ans = None
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            end = mid - 1
            ans = mid
        elif A[mid] > B:
            end = mid - 1
        else:
            start = mid + 1
    if ans is not None:
        beginning = ans
    else:
        return [-1, -1]

    start = beginning
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            start = mid + 1
            ans = mid
        elif A[mid] > B:
            end = mid - 1
        else:
            start = mid + 1
    ending = ans

    return [beginning, ending]

print(searchRange([1,2,3,8,8,8,11],8))