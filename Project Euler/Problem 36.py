# Project Euler: Problem 36
# Jonathan Kosasih

#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
#(Please note that the palindromic number, in either base, may not include leading zeros.)
#------------------------------------------------------------------
def answer():
    total = 0
    for index in range(1000000):
        if(isDeciBinaryPalindrome(index)):
            total += index
    return total
        
def isDeciBinaryPalindrome(number):
    stringNum = str(number)
    if(stringNum == stringNum[::-1]):
        binaryNum = bin(number)[2:]
        if(binaryNum == binaryNum[::-1]):
            return True
    return False
    
        
ans = answer()
print(str(ans))