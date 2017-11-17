'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.
Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
'''
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0: # base is zero
            return 0
        if n == 0: # power is zero
            return 1
        if n%2 == 0: # power is even
            return (pow(x,n//2,d)%d * pow(x,n//2,d)%d) %d
        else: # power is odd
             return (pow(x,n//2,d)%d * pow(x,n//2,d)%d * x) %d