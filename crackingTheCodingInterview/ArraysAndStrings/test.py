def compress_string(s1):
    count=1
    new_string = ""

    for idx in range(1, len(s1)):
        if s1[idx]==s1[idx-1]:
            count+=1
        else:
            new_string += s1[idx-1]
            new_string += str(count)
            count = 1
    new_string += s1[idx-1]
    new_string += str(count)
    return new_string




print(compress_string("aababbcc"))