# LeetCode: Problem 5
# Jonathan Kosasih

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
#------------------------------------------------------------------
class Solution(object):
    # initial solution
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: str
        """
        array = []
        palindromes = []
        for char in string:
            for entry in range(len(array)):
                array[entry] += char
                if(array[entry] == array[entry][::-1]):
                    palindromes.append(array[entry])
            array.append(char)
        return print(max(palindromes))
    
    # dynamic programming
    def longestPalindromeDP(self, s):
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in range(n)]
        for i in range(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in range(n-1):
            if(s[i] == s[i+1]):
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
        for j in range(n):
            for i in range(0, j-1):
                if(s[i] == s[j] and DP[i+1][j-1]):
                    DP[i][j] = True
                    if(max_len < j - i + 1):
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans
        
sol = Solution()
example = "babad"
#example = "cbbd"
#sol.longestPalindrome(example)
print(sol.longestPalindromeDP(example))
print("Test complete")