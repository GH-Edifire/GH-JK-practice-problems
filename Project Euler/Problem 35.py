# Project Euler: Problem 35
# Jonathan Kosasih

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?
#------------------------------------------------------------------
def answer():
    isprime = sieve(1000000)
    ans = sum(1
        for i in range(len(isprime))
        if(isCircularPrime(isprime,isprime[i])))
    return str(ans)

def isCircularPrime(primeList,n):
        s = str(n)
        for i in range(len(s)):
            if(int(s[i : ] + s[ : i]) not in primeList):
                return False
        return True
    
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
        
ans = answer()
print(str(ans))