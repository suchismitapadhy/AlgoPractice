def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


def insertion_sort(a):
    for i in range(len(a)):
        j = i
        while j > 0:
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def shell_sort(a):
    h = 1
    while h <= len(a) / 3:
        h = 3 * h + 1  # in the test use 4 as increment sequence
    while h >= 1:
        for i in range(len(a)):
            j = i
            while j >= h and a[j] < a[j - h]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h /= 3


def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


def quick_sort(array):
    return quick_sort([x for x in array[1:] if x < array[0]]) + [array[0]] \
           + quick_sort([x for x in array[1:] if x >= array[0]]) if array else []


if __name__ == '__main__':
    a = [7, 10, 1, 1, 3, 4, 5, 9, 2, 8]
    b = {}
    for i in range(1, 6):
        b['test' + str(i)] = a[:]
    # Test the three simple sortings
    insertion_sort(b['test1'])  # 1
    selection_sort(b['test2'])  # 2
    shell_sort(b['test3'])  # 3
    print
    b
    # Test the sortings that requires recursion
    print
    merge_sort(b['test4'])  # 4
    print
    quick_sort(b['test5'])  # 5
    # Timsort that is native in Python
    a.sort()  # 6
    print
    a