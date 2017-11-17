def lengthOfLastWord(A):
    # split the string by space and store in list
    # return the last word
    # hellow orld"
    word = ""
    wordlist = []
    flag = False
    for idx in range(len(A) - 1, -1, -1):
        if A[idx] == " ":
            if flag == False:
                continue
            else:
                wordlist.append(word)
                break
        else:
            word += A[idx]
            flag = True

    wordlist.append(word)
    if len(wordlist) == 0:
        return 0
    return len(wordlist[-1])

A= "Hello wo rld  "
print(lengthOfLastWord(A))