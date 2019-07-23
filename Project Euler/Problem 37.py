# Project Euler: Problem 37
# Jonathan Kosasih

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
#from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
#Similarly we can work from right to left: 3797, 379, 37, and 3.
#
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#------------------------------------------------------------------
import eulerlib, itertools, sys
def answer():
    # sum of the filter with trucatable function, starting at 10 and going until the filter/sum has added 11 numbers
    ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
    return str(ans)

def is_truncatable_prime(n):
    # Test if left-truncatable
    i = 10
    while i <= n:
        if not eulerlib.is_prime(n % i):
            return False
        i *= 10
    
    # Test if right-truncatable
    while n > 0:
        if not eulerlib.is_prime(n):
            return False
        n //= 10
    return True
        
ans = answer()
print(str(ans))