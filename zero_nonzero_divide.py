def zero_nonzero_divide(arr):
    i = 0
    j = len(arr)-1
    count=0
    while i <= j:
        if arr[i]!=0:
            i+=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
            count+=1
    return arr,i


A = [0,2,0,0,3,0,6,8,0,5,0]
print(zero_nonzero_divide(A))


