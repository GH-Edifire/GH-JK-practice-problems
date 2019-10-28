# LeetCode: Problem 139
# Jonathan Kosasih

#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
#determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
#Note:
#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
#
#Example 1:
#Input: s = "leetcode", wordDict = ["leet", "code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".
#
#Example 2:
#Input: s = "applepenapple", wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#             Note that you are allowed to reuse a dictionary word.
#             
#Example 3:
#Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#Output: false
#------------------------------------------------------------------
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # sliding window check for any words in word dictionary
                # mark last letter of window if it is a word AND the letter before it was true OR if this is the first word
                if(word == s[i-len(word)+1:i+1] and (memo[i-len(word)] or i-len(word) == -1)):
                    memo[i] = True
        # true only if the last letter makes a word, just report the last letter's status
        return memo[-1]

sol = Solution()
example = "leetcode"
wordDict = ["leet", "code"]
print(str(sol.wordBreak(example, wordDict)))