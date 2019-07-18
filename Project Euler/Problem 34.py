# Project Euler: Problem 34
# Jonathan Kosasih

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#------------------------------------------------------------------
import math
def answer():
    total = 0
    # precompute factorials
    products = [math.factorial(x) for x in range(0,10)]
    
    # https://en.wikipedia.org/wiki/Factorion
    # If n is a natural number of d digits that is a factorion, then 10d − 1 ≤ n ≤ 9!d
    # upper bound will initally be 9,999,999, because 8 or more digits will fail the initial condition
    # but it can be reduced further to the max sum of factorials in a 7-digit number = 2,540,160
    # ***you can reduce it more but that requires even more analysis
    upperbound = math.factorial(9) * 7 
    for i in range(3,upperbound):
        digitSum = 0
        for digit in str(i):
            digitSum += products[int(digit)]
        if(digitSum == i):
            total += i
    return total
        
ans = answer()
print(str(ans))