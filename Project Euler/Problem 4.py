# Project Euler: Problem 4
# Jonathan Kosasih

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
#------------------------------------------------------------------
def largestPalindrome():
    listStrings = []
    for i in range(1000,100,-1):
        for j in range(1000,100,-1):
            string = i * j
            if(checkPalindrome(str(string))):
                listStrings.append(string)
    return max(listStrings)
        
def checkPalindrome(string = ""):
    if(string == string[::-1]):
        return True
    return False

print(largestPalindrome())