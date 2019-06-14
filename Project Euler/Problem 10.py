# Project Euler: Problem 10
# Jonathan Kosasih

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.
#------------------------------------------------------------------
import math
def sumPrime():
    array = [2]
    test = 3
    flag = True
    sumOfPrimes = 2
    while(test < 2000000):
        limit = math.sqrt(test)
        for entry in array:
            if(entry > limit):
                break
            if(test % entry == 0):
                flag = False
                break
        if(flag == True):
            array.append(test)
            sumOfPrimes += test
        test += 1
        flag = True
            
    return print(sumOfPrimes)

sumPrime()
print("Test complete")