# Project Euler: Problem 31
# Jonathan Kosasih

#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?
#------------------------------------------------------------------
def answer():
    total = 200
    COINS = [1,2,5,10,20,50,100,200]
    # DP, initially only 1 way to get 0 (no coins), rest is 0 ways for now
    dp = [1] + [0] * total
    for coin in COINS:
        for index in range(len(dp) - coin):
            # each index is calculated by adding the ways from a previous index
            dp[index + coin] += dp[index]
    return dp[-1]
    
ans = answer()
print(str(ans))
