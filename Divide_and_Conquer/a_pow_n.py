# Qn: Implement a^n using minimum number of multiplication

def pow(a, n):
    # base condition
    if n==0:
        return 1
    # when even
    if n%2==0:
        return pow(a,n/2)*pow(a,n/2)
    # when odd
    else:
        return pow(a, n // 2) * pow(a, n // 2) * a


print(pow(2,10))