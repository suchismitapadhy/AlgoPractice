# def maxSubArray(A):
#     ans = A[0]
#     curr_sum = 0
#     for i in range(len(A)):
#         # if after adding the new number I get
#            a negative number then i will break the subarray
#         if curr_sum + A[i] < 0:
#             ans = max(A[i], ans)
#             curr_sum = 0
#         else:
#             curr_sum += A[i]
#             ans = max(ans, curr_sum)
#     return ans


#--------------------------------------------------
# initialize max_so_far and max_ending_here with first element of the array
# traverse from first element till end
# update  with max of (A[i], max_ending_here+A[i])

def maxSubArray(A):
    max_so_far = A[0]
    curr_max = A[0]

    for i in range(1,len(A)):
        curr_max = max(A[i], curr_max + A[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
B = [5,-3, 8]
A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArray(B))