# Project Euler: Problem 49
# Jonathan Kosasih

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
#but there is one other 4-digit increasing sequence.
#
#What 12-digit number do you form by concatenating the three terms in this sequence?
#------------------------------------------------------------------
import math
import eulerlib
def answer():
    ans = 1487
    while(True):
        ans += 2
        b = ans + 3330
        c = ans + 6660
        if(eulerlib.is_prime(ans) and eulerlib.is_prime(b) and eulerlib.is_prime(c)
           and eulerlib.is_perm(ans,b) and eulerlib.is_perm(b,c)):
            return str(ans) + str(b) + str(c)
ans = answer()
print(str(ans))