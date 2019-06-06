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
    def longestPalindromeDP(self, string):
        if(len(string) < 2 or string == None):
            return string
        
        longest = string[0]
        array = [[False]*len(string)]*len(string)
        for j in range(len(string)):
            array[j][j] = True
            for i in range(j):
                # if the next row/previous column (most recent check) was a palindrome OR its the 2nd letter in substring
                # AND letters on the left and right match of substring, it is also a palindrome
                if((array[i + 1][j - 1] == True or i + 1 > j - 1) and string[i] == string[j]):
                    array[i][j] = True
                    # check for longest substring palindrome
                    # current = right index + left index + 1
                    if(j - i + 1 > len(longest)):
                        longest = string[i:j+1]
        return print(longest)
        
sol = Solution()
example = "babad"
#example = "cbbd"
sol.longestPalindrome(example)
sol.longestPalindromeDP(example)
print("Test complete")