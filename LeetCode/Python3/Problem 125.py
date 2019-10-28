# LeetCode: Problem 125
# Jonathan Kosasih

#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#Note: For the purpose of this problem, we define empty string as valid palindrome.
#------------------------------------------------------------------
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = re.sub('[^a-zA-Z0-9]+','', s)
        string = string.lower()
        reverse = string[::-1]
        if(string == reverse):
            return True
        return False
    
sol = Solution()
example = "A man, a plan, a canal: Panama"
print(str(sol.isPalindrome(example)))
example = "race a car"
print(str(sol.isPalindrome(example)))
