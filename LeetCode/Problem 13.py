# LeetCode: Problem 13
# Jonathan Kosasih

#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#------------------------------------------------------------------
class Solution(object):
    def romanToInt(self, string):
        """
        :type s: str
        :rtype: int
        """
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        precedingChar = ""
        totalValue = 0
        for char in string:
            totalValue += values[char]
            if((char == "V" or char == "X") and precedingChar == "I"):
                totalValue -= 2*values['I']
            elif((char == "L" or char == "C") and precedingChar == "X"):
                totalValue -= 2*values['X']
            elif((char == "D" or char == "M") and precedingChar == "C"):
                totalValue -= 2*values['C']
            precedingChar = char
        return totalValue
                
        
sol = Solution()
example1 = "III"
example2 = "IV"
example3 = "IX"
example4 = "LVIII"
example5 = "MCMXCIV"

print(sol.romanToInt(example1))
print(sol.romanToInt(example2))
print(sol.romanToInt(example3))
print(sol.romanToInt(example4))
print(sol.romanToInt(example5))
