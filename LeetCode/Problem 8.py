# LeetCode: Problem 8
# Jonathan Kosasih

#Implement atoi which converts a string to an integer.

#The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

#The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

#If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

#If no valid conversion could be performed, a zero value is returned.
#Example 1:
#Input: "42"
#Output: 42

#Example 2:
#Input: "   -42"
#Output: -42
#Explanation: The first non-whitespace character is '-', which is the minus sign.
#             Then take as many numerical digits as possible, which gets 42.

#Example 3:
#Input: "4193 with words"
#Output: 4193
#Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

#Example 4:
#Input: "words and 987"
#Output: 0
#Explanation: The first non-whitespace character is 'w', which is not a numerical 
#             digit or a +/- sign. Therefore no valid conversion could be performed.

#Example 5:
#Input: "-91283472332"
#Output: -2147483648
#Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#             Thefore INT_MIN (−2^31) is returned.
#------------------------------------------------------------------
class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        check = ""
        start = False
        string = string.strip()
        for char in string:
            if(char == "-" or char == "+" or char.isdigit()):
                check += char
                start = True
            if(start and char.isalpha()):
                break
            elif(not start and char.isalpha()):
                return 0
        if(check == "-" or check == "+"):
            return 0
        return max(-(2**31),(min(int(check),2**31 - 1)))
        
sol = Solution()
example1 = "42"
example2 = "      -42"
example3 = "4193 with words"
example4 = "words and 987"
example5 = "-91283472332"
example6 = "+"
print(sol.myAtoi(example1))
print(sol.myAtoi(example2))
print(sol.myAtoi(example3))
print(sol.myAtoi(example4))
print(sol.myAtoi(example5))
print(sol.myAtoi(example6))