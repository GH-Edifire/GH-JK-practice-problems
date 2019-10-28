# LeetCode: Problem 17
# Jonathan Kosasih

#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#Example:
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#------------------------------------------------------------------
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        array = []
        buttons = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        for num in digits:
            if(len(array) == 0):
                for letter in buttons.get(num):
                    array.append(letter)
            else:
                placeholder = []
                for entry in array:
                    for letter in buttons.get(num):
                        placeholder.append(entry+letter)
                array = placeholder.copy()
        return array
        
sol = Solution()
example = "23"
print(sol.letterCombinations(example))
print("# of combinations: " + str(len(sol.letterCombinations(example))))