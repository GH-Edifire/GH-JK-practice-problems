# LeetCode: Problem 171
# Jonathan Kosasih

#Given a column title as appear in an Excel sheet, return its corresponding column number.
#
#For example:
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 
#    ...
#------------------------------------------------------------------
import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s):
            return 0
        dictionary = {letter:index for index, letter in enumerate(string.ascii_uppercase, start = 1)}
        s_length = len(s)-1
        number = 0
        for i in range(s_length, -1, -1):
            number += dictionary[s[i]] * 26**(s_length-i)
        return number
        
sol = Solution()
example = "A"
print(str(sol.titleToNumber(example)))
example = "AA"
print(str(sol.titleToNumber(example)))
example = "AB"
print(str(sol.titleToNumber(example)))
example = "ZY"
print(str(sol.titleToNumber(example)))
example = "CB"
print(str(sol.titleToNumber(example)))
example = "BAC"
print(str(sol.titleToNumber(example)))