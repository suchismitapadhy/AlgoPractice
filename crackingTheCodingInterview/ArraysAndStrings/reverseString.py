#method 1
def reverse_string(s1):
    #string is immutable so first putting it in a list
    s1 = list(s1)
    # initialize two pointers
    i = 0
    j = len(s1)-1
    while i<j:
        # swapping the elements
        s1[i],s1[j] = s1[j],s1[i]
        i+=1
        j-=1
    return "".join(s1)

#method 2
def reverse_string_1(s1):
    return s1[::-1]

#method 3
def reverse_string_2(s1):
    s1_string = ""
    for i in range(len(s1)-1,-1,-1):
        s1_string+=s1[i]
    return s1_string

print(reverse_string("radha"))
print(reverse_string_1("radha"))
print(reverse_string_2("radha"))

#time complexity o(n)
#space complexity o(n)





