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
        highestCount = 0
        count = 0
        highestSubString = ""
        subString = ""
        stringSet = set("") # Found out later you dont even need to declare a set, just check if a char is in the subString
        for char in string:
            if(char in stringSet):
                if(count > highestCount):
                    highestCount = count
                    highestSubString = subString
                    count = 1
                    subString = char
                    stringSet.clear()
                    stringSet.add(char)
                else:
                    count = 1
                    subString = ""
            else:  
                subString += char
                stringSet.add(char)
                count += 1
        
        return highestCount, highestSubString
            
sol = Solution()
#example = "abcabcbb"
#example = "bbbbb"
example = "pwwkew"
print("Input: \"" + example +"\"")
answer = sol.lengthOfLongestSubstring(example)
print("Output: " + str(answer[0]))
print("Explanation: The answer is \"" + answer[1] + "\", with the length of " + str(answer[0]))