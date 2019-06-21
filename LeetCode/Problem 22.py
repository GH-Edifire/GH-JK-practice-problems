# LeetCode: Problem 22
# Jonathan Kosasih

#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#For example, given n = 3, a solution set is:
#
#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]
#------------------------------------------------------------------
# patterns
# n = 1, "()"
# n = 2, "(()), ()()"
# n = 3,
# case 1: take list at n-1 and place () at the ends
# "((()))" = ( + dynamic[2][0] + )
# "(()())" = ( + dynamic[2][1] + )
# case 2: combine lists from dynamic[1] to dynamic[n-1] to get combinations for n
#         make sure it adds up to n, example == 1 + 2 = 3
# "()(())" = dynamic[1][0] + dynamic[2][0]
# "()()()" = dynamic[1][0] + dynamic[2][1]
# "(())()" = dynamic[2][0] + dynamic[1][0]
# IGNORE DUPLICATES, JUST GET UNIONS (get uniques)
# example = "()()()" = dynamic[2][1] + dynamic[1][0] but we already got that result before so ignore it
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # base cases
        dynamic = {1:["()"], 2:["(())", "()()"]}
        # do other cases
        for i in range(3, n+1):
            dynamic[i] = set(["(" + x + ")" for x in dynamic[i-1]])
            for j in range(1,i):
                dynamic[i] = dynamic[i].union([x+y for x in dynamic[j] for y in dynamic[i-j]])
        return list(dynamic[n])

sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(4))