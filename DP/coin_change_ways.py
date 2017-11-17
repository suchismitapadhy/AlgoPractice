def coin_change(target, denominations):
    # build an array of size target+1 with 0's
    matrix = [0 for i in range(target+1)]
    #initialize 0th index as 1--> there is one way to construct 0 coins
    matrix[0]=1
    # pick a coin from your purse
    # for all values in your array that are >=this coin will be affected
    # To get the no. of ways using this coin we shall update the current ways + (index-coin) ways
    # for any target, the new no.of ways after considering this coin = the number of ways without considering this coin + no. of ways to create target-coin ways
    for coin in denominations:
        for index in range(coin,target+1):
            matrix[index]+=matrix[index-coin]
    return matrix[-1]


print(coin_change(10,[1,2,5]))