
def sqrt(A):
    if A == 0 or A == 1:
        return A
    start = 1
    end = A
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == A:
            return mid
        if mid * mid < A:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

print(sqrt(328963471))

# Algorithm:
# 1) Start with 'start' = 0, end = 'x',
# 2) Do following while 'start' is smaller than or equal to 'end'.
#       a) Compute 'mid' as (start + end)/2
#       b) compare mid*mid with x.
#       c) If x is equal to mid*mid, return mid.
#       d) If x is greater, do binary search between mid+1 and end. In this case, we also update ans (Note that we need floor).
#       e) If x is smaller, do binary search between start and mid-1


