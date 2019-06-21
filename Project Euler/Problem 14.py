# Project Euler: Problem 14
# Jonathan Kosasih

#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
#------------------------------------------------------------------
import sys
sys.setrecursionlimit(3000)

dynamic = {}
def collatz(number):
    if(not number in dynamic):
        if(number == 1):
            dynamic[number] = 1
        elif(number % 2 == 0):
            dynamic[number] = collatz(number // 2) + 1
        else:
            dynamic[number] = collatz(3*number + 1) + 1
    return dynamic[number]
def answer():
    ans = max(range(1,1000000), key=collatz)
    return ans
print(answer())
print("Test complete")