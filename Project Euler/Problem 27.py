# Project Euler: Problem 27
# Jonathan Kosasih

#Considering quadratics of the form:
#
#n2+an+b, where |a|<1000 and |b|≤1000
#
#where |n| is the modulus/absolute value of n
#e.g. |11|=11 and |−4|=4
#
#Find the product of the coefficients, a and b,
#for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
#------------------------------------------------------------------
# n2+an+b
# f(0) = 0+0+b
# b must be a prime number and positive

# testing a's
# n2+(0)n+13, f(0) = PRIME, f(1) = NOT PRIME
# n2+(1)n+13, f(0) = PRIME, f(1) = NOT PRIME
# n2+(2)n+13, f(0) = PRIME, f(1) = NOT PRIME
# n2+(3)n+13, f(0) = PRIME, f(1) = PRIME, f(2) = PRIME, f(3) = PRIME, f(4) = PRIME, f(5) = PRIME..., f(8) = PRIME, f(9) = NOT PRIME
# n2+(4)n+13, f(0) = PRIME, f(1) = NOT PRIME
# n2+(5)n+13, f(0) = PRIME, f(1) = PRIME, f(2) = NOT PRIME

# a's can be composite or prime, but primes always will yield more prime results than when a is composite, so just check
# when a is prime as well

def answer():
    #primes below 1000
    primes1000 = sieve(1000)

    #copy of primes1000 variable
    primes = primes1000[:]

    #assume the largest value is 0 at start
    largest = 0

    #looping through a quadratic equation
    for b in primes1000:
        for a in primes1000:
            i = 0
            #positive a and b
            while True:
                quadratic = i**2+a*i+b
                if(quadratic not in primes):
                    if(is_prime(quadratic)):
                        primes.append(quadratic)
                    else:
                        if(i-1 > largest):
                            largest = i-1
                            axb = a*b
                        break
                i += 1
            i = 0
            #negative a and positive b
            while True:
                quadratic = i**2-a*i+b
                if(quadratic not in primes):
                    if(is_prime(quadratic) and quadratic>0):
                        primes.append(quadratic)
                    else:
                        if(i-1 > largest):
                            largest = i-1
                            axb = -1*a*b
                        break
                i += 1
    return axb

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5+1)):
        index = i*2
        while(index < n):
            is_prime[index] = False
            index = index+i
    prime = []
    for i in range(n):
        if(is_prime[i] == True):
            prime.append(i)
    return prime

def is_prime(n):
    """function to check if the number
    is prime or not"""
    for i in range(2,int(abs(n)**0.5)+1):
        if(n%i == 0):
            return False
    return True

ans = answer()
print(str(ans))
