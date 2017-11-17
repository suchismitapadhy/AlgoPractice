class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        # number of ways for n = 0
        numways_arr = [1]
        # fill the ways array for n = 1 to n
        for numw in range(1, A+1):
            # n = 1
            if numw == 1:
                numways_arr.append(numways_arr[numw-1])
            if numw > 1:
                numways_arr.append(numways_arr[numw-1] +  numways_arr[numw-2])

        return numways_arr[-1]