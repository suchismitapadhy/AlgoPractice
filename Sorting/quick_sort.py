# Choose pivots at random

def quick_sort_driver(A):
    quick_sort(A, start=0, finish=len(A) - 1)


def quick_sort(a, start, finish):
    if start < finish:  # if partitionIndex is the 1st element then left hand there is no array to sort
        partitionIndex = partition(a, start, finish)
        # print(a[partitionIndex])
        quick_sort(a, start, partitionIndex - 1)
        quick_sort(a, partitionIndex + 1, finish)

def partition(a, start, finish):
    pivot = finish

    while start < finish:  # continue till start < finish
        if a[start] < a[pivot]:  # if the start element < pivot then move start forward
            start += 1
        else:  # if start < pivot,
            a[finish - 1], a[start] = a[start], a[finish - 1]  # take finish-1 and swap with start
            finish -= 1  # reduce finish
    a[pivot], a[finish] = a[finish], a[pivot]
    return start







A = [1,2,7,3,4,23,11,5]
#start = 0th item
#finish = last item
#inplace so changes array A
quick_sort_driver(A)
print(A)

# Time complexity: (n log n)
# worst case: sorted array n^2 --> divides into n-1 and 0
# average case = best case

# instead of taking startindex/endIndex as pivots take random pivots --> break the sorted structure




