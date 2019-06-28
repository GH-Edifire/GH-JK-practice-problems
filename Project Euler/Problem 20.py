# Project Euler: Problem 20
# Jonathan Kosasih

#n! means n × (n − 1) × ... × 3 × 2 × 1
#
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!
#------------------------------------------------------------------
import math
def answer():
    n = math.factorial(100)
    ans = sum(int(char) for char in str(n))
    return ans

print(str(answer()))
print("Test complete")