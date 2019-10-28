# LeetCode: Problem 122
# Jonathan Kosasih

#Say you have an array for which the ith element is the price of a given stock on day i.
#
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like
#(i.e., buy one and sell one share of the stock multiple times).
#
#Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
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
        for i in range(1,len(prices)):
            if(prices[i] > prices[i-1]):
                profit += prices[i] - prices[i-1]
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