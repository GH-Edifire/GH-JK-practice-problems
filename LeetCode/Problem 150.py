# LeetCode: Problem 150
# Jonathan Kosasih

#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#Note:
#Division between two integers should truncate toward zero.
#The given RPN expression is always valid.
#That means the expression would always evaluate to a result and there won't be any divide by zero operation.
#------------------------------------------------------------------
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if(not tokens):
            return 0
        stack = []
        for token in tokens:
            if(token == "+"):
                tempOne = stack.pop()
                tempTwo = stack.pop()
                stack.append(tempTwo + tempOne)
            elif(token == "-"):
                tempOne = stack.pop()
                tempTwo = stack.pop()
                stack.append(tempTwo - tempOne)
            elif(token == "*"):
                tempOne = stack.pop()
                tempTwo = stack.pop()
                stack.append(tempTwo * tempOne)
            elif(token == "/"):
                tempOne = stack.pop()
                tempTwo = stack.pop()
                stack.append(int(tempTwo / tempOne))
            else:
                stack.append(int(token))
        return stack.pop()
        
sol = Solution()
example = ["2", "1", "+", "3", "*"]
print(str(sol.evalRPN(example)))
example = ["4", "13", "5", "/", "+"]
print(str(sol.evalRPN(example)))
example = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(str(sol.evalRPN(example)))
example = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(str(sol.evalRPN(example)))