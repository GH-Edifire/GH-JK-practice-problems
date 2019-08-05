# Project Euler: Problem 46
# Jonathan Kosasih

#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2
#
#It turns out that the conjecture was false.
#
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#------------------------------------------------------------------
import eulerlib
import math

# number = prime + 2*(other)^2
# other = ((number - prime)/2)^(1/2)
# other should be a perfect square == integer
def answer():
    num = 3
    primes = [2]
    while(True):
        if(eulerlib.is_prime(num)):
            primes.append(num)
        else:
            for i in primes:
                if(math.sqrt(((num-i)/2)) == int(math.sqrt(((num-i)/2)))):
                    break
            # found a number that doesn't fit Goldbach's conjecture
            else:
                break
        num += 2
    return num
        
ans = answer()
print(str(ans))