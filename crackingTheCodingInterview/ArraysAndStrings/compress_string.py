def compress_string(s1):
    if len(s1)==0:
        return s1
    newstr = ""
    curr_letter = s1[0]
    curr_count = 1
    for i in range(1,len(s1)):
        if s1[i]==curr_letter:
            curr_count+=1
        else:
            newstr+=curr_letter
            newstr+=str(curr_count)
            curr_letter = s1[i]
            curr_count = 1
    # end of string is also a chenge
    newstr += curr_letter
    newstr += str(curr_count)
    return newstr

print(compress_string("aababbcc"))

# Algo:
# maintain a curr_letter and curr_count of that letter
# traverse through the string to check if item == curr_letter:
#     if yes-- then keep incrementing count
#     if no -- add to new string the curr_letter and curr_count
#           -- make the item as new curr_letter n start curr_count from 1




