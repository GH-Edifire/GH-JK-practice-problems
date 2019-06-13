# LeetCode: Problem 14
# Jonathan Kosasih

#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
#Example 1:
#
#Input: ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#
#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
#------------------------------------------------------------------
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(strs == None):
            return "\"\""
        prefix = min(strs,key=len)
        for index in range(len(prefix)):
            for entry in strs:
                if(entry[index] != prefix[index]):
                    return prefix[:index] if index > 0 else "\"\""
   
sol = Solution()
example1 = ["flower","flow","flight"]
example2 = ["dog","racecar","car"]
print(sol.longestCommonPrefix(example1))
print(sol.longestCommonPrefix(example2))