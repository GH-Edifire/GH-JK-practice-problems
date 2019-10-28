# LeetCode: Problem 300
# Jonathan Kosasih

#Given an unsorted array of integers, find the length of longest increasing subsequence.
#
#Example:
#Input: [10,9,2,5,3,7,101,18]
#Output: 4 
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
#Note:
#There may be more than one LIS combination, it is only necessary for you to return the length.
#Your algorithm should run in O(n2) complexity.
#------------------------------------------------------------------
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if(not nums or len(nums) == 0):
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        ans = 1
        for i in range(1,len(nums)):
            maxVal = 0
            for j in range(i):
                if(nums[i] > nums[j]):
                    maxVal = max(maxVal, dp[j])
            dp[i] = maxVal + 1
            ans = max(ans, dp[i])
        return ans

sol = Solution()
example = [10,9,2,5,3,7,101,18]
print(str(sol.lengthOfLIS(example)))