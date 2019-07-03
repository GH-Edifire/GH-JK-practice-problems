# Project Euler: Problem 23
# Jonathan Kosasih

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
#For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
#the smallest number that can be written as the sum of two abundant numbers is 24.
#By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
#the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it
#is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#------------------------------------------------------------------
import math
def answer():
    limit = 28123 + 1
    abundant = [False] * limit
    total = 0
    # sum every number, mark if a number is abundant
    for index in range(1, limit):
        total += index
        if(sum_div(index) > index):
            abundant[index] = True
            
    # check each number if it is a sum of two abundant numbers, use built truth table
    # Example: index = 24, index2 = 12, abundant[12] = True, abundant[24 - 12] = True,
    # therefore 24 is a sum of two abundant numbers
    for index in range(1,limit):
        for index2 in range (1, index+1):
            if(abundant[index2] and abundant[index - index2]):
                # number is a sum of two abundant numbers, subtract from total
                total -= index
                break
        
    return total

# from P21, sums divisors of a number
def sum_div(n):
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

ans = answer()
print(str(ans))
