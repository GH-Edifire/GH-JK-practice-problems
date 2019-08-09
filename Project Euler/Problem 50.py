# Project Euler: Problem 50
# Jonathan Kosasih

#The prime 41, can be written as the sum of six consecutive primes:
#
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most consecutive primes?
#------------------------------------------------------------------
import math
import eulerlib
def answer():
    primes = eulerlib.list_primes(1000000)
    length = 0
    max = 0
    lastj = len(primes)
    for i in range(len(primes)):
        for j in range(i+length, lastj):
            result = sum(primes[i:j])
            if(result < 1000000):
                if(result in primes):
                    length = j-i
                    max = result
            else:
                lastj = j+1
                break
    return max
    
ans = answer()
print(str(ans))