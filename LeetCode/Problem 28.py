# LeetCode: Problem 28
# Jonathan Kosasih

#Implement strStr().
#
#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#Example 1:
#Input: haystack = "hello", needle = "ll"
#Output: 2
#
#Example 2:
#Input: haystack = "aaaaa", needle = "bba"
#Output: -1
#
#Clarification:
#What should we return when needle is an empty string? This is a great question to ask during an interview.
#
#For the purpose of this problem, we will return 0 when needle is an empty string.
#This is consistent to C's strstr() and Java's indexOf().
#------------------------------------------------------------------
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(haystack is None or haystack == ""):
            return 0
        index = 0
        while(index < (len(haystack) - len(needle)+1)):
            if(haystack[index:(index+len(needle))] == needle):
                return index
            index += 1
        return -1

sol = Solution()
haystack = "hello"
needle = "ll"
print(str(sol.strStr(haystack, needle)))

haystack = "aaaaa"
needle = "bba"
print(str(sol.strStr(haystack, needle)))

haystack = ""
needle = "aaa"
print(str(sol.strStr(haystack, needle)))