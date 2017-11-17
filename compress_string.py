def compress_string(astr):
    count = 1
    mygenerated_string = ""
    for i in range(1, len(astr)):

        if astr[i] == astr[i - 1]:
            count += 1
        else:
            mygenerated_string += astr[i - 1] + str(count)
            count = 1
    mygenerated_string += astr[i - 1] + str(count)

    if len(mygenerated_string) <= len(astr):
        return mygenerated_string
    else:
        return astr


print(compress_string("aabccccaaa"))