# LeetCode: Problem 3
# Jonathan Kosasih

# Given a string, find the length of the longest substring without repeating characters.# The digits are stored in reverse order and each of their nodes contain a single digit.

# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#------------------------------------------------------------------
class Solution(object):
    def lengthOfLongestSubstring(self, string):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(string)):
            if string[i] in usedChar and start <= usedChar[string[i]]:
                start = usedChar[string[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[string[i]] = i

        return maxLength            
sol = Solution()
#example = "abcabcbb"
#example = "bbbbb"
example = "pwwkew"
example = " "
print("Input: \"" + example +"\"")
answer = sol.lengthOfLongestSubstring(example)
print(str(answer))