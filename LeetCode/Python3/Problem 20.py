# LeetCode: Problem 20
# Jonathan Kosasih

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
#Example 1:
#Input: "()"
#Output: true
#
#Example 2:
#Input: "()[]{}"
#Output: true
#
#Example 3:
#Input: "(]"
#Output: false
#
#Example 4:
#Input: "([)]"
#Output: false
#
#Example 5:
#Input: "{[]}"
#Output: true
#------------------------------------------------------------------
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if(char == "(" or char == "{" or char == "["):
                stack.append(char)
            else:
                if(len(stack) == 0):
                    return False
                test = stack.pop()
                if((char == ")" and test != "(") or (char == "}" and test != "{") or (char == "]" and test != "[")):
                    return False
        if(len(stack) == 0):
            return True
        return False
    
    # looks a bit cleaner
    def isValidAlt(self,s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        
sol = Solution()
example1 = "()"
example2 = "()[]{}"
example3 = "(]"
example4 = "([)]"
example5 = "{[]}"
example6 = "]"
print(sol.isValid(example1))
print(sol.isValid(example2))
print(sol.isValid(example3))
print(sol.isValid(example4))
print(sol.isValid(example5))
print(sol.isValid(example6))