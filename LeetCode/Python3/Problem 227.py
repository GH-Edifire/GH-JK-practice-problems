# LeetCode: Problem 227
# Jonathan Kosasih

#Implement a basic calculator to evaluate a simple expression string.
#
#The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
#The integer division should truncate toward zero.
#
#Example 1:
#Input: "3+2*2"
#Output: 7
#
#Example 2:
#Input: " 3/2 "
#Output: 1
#
#Example 3:
#Input: " 3+5 / 2 "
#Output: 5
#
#Note:
#You may assume that the given expression is always valid.
#------------------------------------------------------------------
import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s):
            return 0
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            if(s[i].isdigit()):
                num = num * 10 + int(s[i])
            if(s[i] in "*/-+" or i == len(s)-1):
                if(sign == "-"):
                    stack.append(-num)
                elif(sign == "+"):
                    stack.append(num)
                elif(sign == "*"):
                    stack.append(stack.pop()*num)
                else:
                    temp = stack.pop()
                    if(temp // num < 0 and temp % num != 0):
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign = s[i]
                num = 0
        return sum(stack)
    def calculateAlt(self,s):
        tokens = iter(re.findall('\d+|\S', s))
        total, sign = 0, 1
        for token in tokens:
            if(token in '+-'):
                total += sign * term
                sign = ' +'.find(token)
            elif(token in '*/'):
                n = int(next(tokens))
                term = term*n if token == '*' else term//n
            else:
                term = int(token)
        return total + sign * term
        
sol = Solution()
string = "3+2*2"
print(str(sol.calculate(string)))
string = " 3/2 "
print(str(sol.calculate(string)))
string = " 3+5 / 2 "
print(str(sol.calculate(string)))
string = " 0 "
print(str(sol.calculate(string)))
string = "42"
print(str(sol.calculate(string)))
string = "1 + 1"
print(str(sol.calculate(string)))
string = "1+1+1"
print(str(sol.calculateAlt(string)))