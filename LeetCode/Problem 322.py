# LeetCode: Problem 322
# Jonathan Kosasih

#You are given coins of different denominations and a total amount of money amount.
#Write a function to compute the fewest number of coins that you need to make up that amount.
#If that amount of money cannot be made up by any combination of the coins, return -1.
#
#Example 1:
#Input: coins = [1, 2, 5], amount = 11
#Output: 3 
#Explanation: 11 = 5 + 5 + 1
#
#Example 2:
#Input: coins = [2], amount = 3
#Output: -1
#
#Note:
#You may assume that you have an infinite number of each kind of coin.
#------------------------------------------------------------------
class Solution:
    def coinChange(self, coins, amount):
        if(not coins):
            return -1
        if(amount == 0):
            return 0
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if(i >= coin):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] > amount else dp[amount]

sol = Solution()
coins = [1, 2, 5]
amount = 11
print(str(sol.coinChange(coins, amount)))
coins = [2]
amount = 3
print(str(sol.coinChange(coins, amount)))
coins = [1]
amount = 0
print(str(sol.coinChange(coins, amount)))
coins = [2,5,10,1]
amount = 27
print(str(sol.coinChange(coins, amount)))