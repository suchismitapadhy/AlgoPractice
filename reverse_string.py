def reverse_string(s1, s2):
    if len(s1)!=len(s2):
        return False
    #constructed mydict with s1
    mydict = {}
    for i in s1:
        mydict[i] = mydict.get(i,0)+1
    # decrement mydict from s2
    for i in (s2):
        if i in mydict:
            mydict[i]-=1
        else:
            return False
    #verify all key have 0 as value
    for k in mydict:
        if mydict[k]!=0:
            return False
        else:
            return True

def main():
    print(reverse_string("radha", "adhas"))

main()