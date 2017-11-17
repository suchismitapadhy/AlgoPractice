# 1) Problem
# solving
# Let’s
# an
# integer
# array
# A
# of
# dimension
# n and an
# array
# P
# of
# floating - point
# numbers
# between
# 0 and 1
# whose
# sum is equal
# to
# 1 and of
# dimension
# n
# also.
#     Write
# a
# routine
# randomInteger
# that
# output
# one
# element
# of
# A
# every
# time
# it is called,
# with the corresponding probability in the float array
# You have at your disposal  the routine “ float  frand()”  that output a floating-point number between[0, 1[with a constant distribution every time it is called
#
# Example:
#     n = 5
# A = 1
# 5
# 3
# 6
# 8
# P = 0.2
# 0.2
# 0.1
# 0.4
# 0.1
#
# The
# routine
# needs
# to
# output in average
# the
# number
# 5
# 20 % of
# time, the
# number
# 6
# 40 % of
# the
# time …
#
# Please
# write
# a
# generic
# routine in C / C + + or Python
# that
# can
# handle
# any
# case(i.e for any value
# n)
# Some
# questions
# to
# think
# about:
# -What is the
# complexity
# of
# your
# algorithm? Worst
# case, Best
# case, average
# case
# - How
# can
# you
# optimize
# it


def binary_search(A, num):
    start = 0
    end = len(A) - 1
    while start < end:
        mid = start + (end - start + 1) / 2
        if A[mid] == num:
            return mid
        elif A[mid] > num:
            start = mid + 1
        else:
            end = mid - 1
    return start


sum_array = []
sum_value = 0
for i in P:
    sum_value += i
    sum_array.append(sum_value)


def randomInteger(A, sum_array):
    num = frand()
    i = binary_search(sum_array, num)
    for i in range(len(sum_array)):
        if sum_array[i] < num:
            continue
        else:
            break
    return A[i]