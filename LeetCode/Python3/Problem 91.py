# LeetCode: Problem 91
# Jonathan Kosasih

#A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
#Example 1:
#
#Input: "12"
#Output: 2
#Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#Example 2:
#
#Input: "226"
#Output: 3
#Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#------------------------------------------------------------------
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s or s[0] == "0"):
            return 0
        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if(0 < int(s[0]) <= 9) else 0
        
        for i in range(2, len(s) + 1):
            if(0 < int(s[i-1:i]) <= 9):
                dp[i] += dp[i-1]
            if(s[i-2:i][0] != "0" and 0 < int(s[i-2:i]) <= 26):
                dp[i] += dp[i-2]
        return dp[len(s)]
        
sol = Solution()
example = "227"
print(str(sol.numDecodings(example)))