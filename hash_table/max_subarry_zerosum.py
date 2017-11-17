# maximum contiguous sub array that sums to zero

def max_subarray_zerosum(A):
    #initialize a hash table
    my_dict = {}
    # maintain a rolling sum
    # initialize variables
    rollover = 0
    max_len = 0
    max_subarray = (-1,-1)
    # go through the array to make rolling sum
    # if rolling sum value already exist in the hastable --> we got a subarray that sums to 0
    #                                                       we need to track this and also check if this subarray is max length
    #                                                       what we need to track? max_len and also sub array A[start:end]
    # else -->  add in hash table
    for idx in range(0,len(A)):
        rolling_sum = A[idx] + rollover
        if rolling_sum in my_dict:
            curr_len = idx - my_dict[rolling_sum]
            curr_subarray = (my_dict[rolling_sum]+1, idx)
            if curr_len > max_len:
                max_len = curr_len
                max_subarray = curr_subarray

        else:
            my_dict[rolling_sum]=idx
    return max_subarray

A = [15, -2, 2, -8, 1, 7, 10, 23]
start, end =max_subarray_zerosum(A)

print(A[start:end+1])
