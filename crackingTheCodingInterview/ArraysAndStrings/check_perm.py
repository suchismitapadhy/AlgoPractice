def check_perm(s1, s2):
    # traverse through s1 and populate bin dictionary
    # traverse through s2;
    # if item not in dict: then false
    # if item in dictionary: decrement the value
    # if the value becomes zero: delete the key
    # traverse through the dictionary to check length is zero--> see if it is empty

    #initialize the dict
    mydict = {}
    #populate the dict with s1 char
    for char in s1:
        mydict[char]=mydict.get(char,0)+1
    #traverse through s2
    for item in s2:
        #check if item exists:
        if item in mydict:
            mydict[item]-=1
            #check if value is zero; if yes delete the key
            if mydict[item]==0:
                del mydict[item]
        else:
            return False
    # check if len(Dict) == o
    if len(mydict)==0:
        return True
    else:
        return False

print(check_perm("radha","adhar"))


