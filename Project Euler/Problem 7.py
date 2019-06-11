# Project Euler: Problem 7
# Jonathan Kosasih

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#------------------------------------------------------------------
import math
def nthPrime(number):
    array = [2]
    test = 3
    flag = True
    while(len(array) < number):
        limit = math.sqrt(test)
        for entry in array:
            if(entry > limit):
                break
            if(test % entry == 0):
                flag = False
                break
        if(flag == True):
            array.append(test)
        test += 1
        flag = True
            
    return print(str(array[number-1]))
    
#nthPrime(6)
nthPrime(10001)
print("Test Complete")