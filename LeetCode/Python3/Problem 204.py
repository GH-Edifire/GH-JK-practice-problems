# LeetCode: Problem 204
# Jonathan Kosasih

#Count the number of prime numbers less than a non-negative number, n.
#
#Example:
#Input: 10
#Output: 4
#Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#------------------------------------------------------------------
class Solution(object):
    # initial solution, very slow but works
    def countPrimesINITIAL(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(not n or n <= 2):
            return 0
        primes = [2]
        for i in range(3, n):
            primeCheck = True
            limit = int(i ** 0.5)
            for prime in primes:
                # early stop when checking primes
                if(prime > limit):
                    break
                if(i % prime == 0):
                    primeCheck = False
                    break
            if(primeCheck == True):
                primes.append(i)
                    
        return len(primes)
    
    # optimized with Sieve of Eratosthenes
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(not n or n < 3):
            return 0
        primes = [True] * n
        # numbers 0 and 1 are not primes
        primes[0] = False
        primes[1] = False
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if(primes[i]):
                # mark off all multiples of i as nonprime
                # primes[i*i: n: i] will grab the indexes/memory location of the multiples
                # [False] * len(primes[i*i: n: i]) will give how many to mark as false
                primes[i*i: n: i] = [False] * len(primes[i*i: n: i])
        return sum(primes)

sol = Solution()
example = 10
print(str(sol.countPrimes(example)))