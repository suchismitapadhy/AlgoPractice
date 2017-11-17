class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0:
            return []
        numrows = A
        arr = [[1]]
        for _ in range(numrows - 1):
            new_arr = [1]
            for i in range(len(arr[-1]) - 1):
                new_arr.append(arr[-1][i] + arr[-1][i + 1])
            new_arr.append(1)
            arr.append(new_arr)
        return arr
