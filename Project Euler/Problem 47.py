# Project Euler: Problem 47
# Jonathan Kosasih

#The first two consecutive numbers to have two distinct prime factors are:
#
#14 = 2 × 7
#15 = 3 × 5
#
#The first three consecutive numbers to have three distinct prime factors are:
#
#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#
#Find the first four consecutive integers to have four distinct prime factors each.
#What is the first of these numbers?
#------------------------------------------------------------------
import math
def answer():
    # first number with 4 distinct prime factors
    consec = 2*3*5*7
    while(True):
        if(numPrimeFactors(consec) == 4):
            consec += 1
            if(numPrimeFactors(consec) == 4):
                consec += 1
                if(numPrimeFactors(consec) == 4):
                    consec += 1
                    if(numPrimeFactors(consec) == 4):
                        return consec - 3
        consec += 1

def numPrimeFactors(num):
    i = 2
    primeFactors = set()
    while(i < num**0.5 or num == 1):
        if(num % i == 0):
           num = num // i
           primeFactors.add(i)
           i -= 1
        i += 1
    return len(primeFactors)+1
        
ans = answer()
print(str(ans))