# LeetCode: Problem 121
# Jonathan Kosasih

#Say you have an array for which the ith element is the price of a given stock on day i.
#
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
#design an algorithm to find the maximum profit.
#
#Note that you cannot sell a stock before you buy one.
#
#Example 1:
#
#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#             Not 7-1 = 6, as selling price needs to be larger than buying price.
#Example 2:
#
#Input: [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.
#------------------------------------------------------------------
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(not prices):
            return 0
        profit = 0
        lowest = prices[0]
        for i in range(1,len(prices)):
            if(lowest > prices[i]):
                lowest = prices[i]
            else:
                if((prices[i] - lowest > profit)):
                    profit = max(profit, (prices[i] - lowest))
        return profit
        
    
sol = Solution()
example = [7,1,5,3,6,4]
print(str(sol.maxProfit(example)))
example = [7,6,4,3,1]
print(str(sol.maxProfit(example)))
example = []
print(str(sol.maxProfit(example)))
example = [2,8,1,2]
print(str(sol.maxProfit(example)))