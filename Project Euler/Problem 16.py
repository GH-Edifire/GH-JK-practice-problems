# Project Euler: Problem 16
# Jonathan Kosasih

#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?
#------------------------------------------------------------------
import math
def answer():
    number = 2**1000
    ans = 0
    for digit in str(number):
        ans += int(digit)
    return ans
print(str(answer()))
print("Test complete")