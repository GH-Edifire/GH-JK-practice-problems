# Project Euler: Problem 5
# Jonathan Kosasih

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#------------------------------------------------------------------
import math

# no import needed, slower
def solution(number):
    need = number - number//2
    middle = number//2
    found = 0
    maxNum = 1
    for i in range(1,number+1):
        maxNum *= i
    for i in range(number,maxNum,number):
        for j in range(middle,number):
            if (i % j != 0):
                break
            found += 1
        if(found == need):
            return i
        found = 0
        
# need to import math, but is faster
def solutionImportMath(number):
    answer = 1
    for i in range(1, number + 1):
        answer *= i // math.gcd(i, answer)
    return str(answer)

print(solution(20))
print(solutionImportMath(20))
