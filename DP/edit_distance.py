def edit_distance(S1, S2):
    #initialize the table
    a = len(S1)+1
    b = len(S2)+1
    table = [[-1 for i in range(a)] for j in range(b)]
    for i in range(0,a):
        table[0][i]=i
    for i in range(0,b):
        table[i][0]=i

    for i in range(1,b):
        for j in range(1, a):
            if S2[i-1]==S1[j-1]:
                table[i][j] = min(table[i-1][j], table[i-1][j-1], table[i][j-1])
            else:
                table[i][j] = min(table[i-1][j], table[i-1][j-1], table[i][j- 1]) + 1
    return table[i][j]






def main():
    S1 = "saturday"
    S2 = "sunday"
    print(edit_distance(S1, S2))
main()