# Project Euler: Problem 3
# Jonathan Kosasih

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
#------------------------------------------------------------------
def largestPrimeFactor(number, primeFactor = 2):
    # keep dividing original number by smallest divisible prime numbers, will result in largest prime
    while(True):
        primeFactor = smallestPrimeFactor(number)
        if(primeFactor < number):
            number = number // primeFactor
        else:
            return number
        
def smallestPrimeFactor(number = 2):
    for i in range(2,number):
        if(number % i == 0):
            # found smallest prime
            return i
    # number itself is already a prime
    return number

#example = 13195
example = 600851475143
print("Largest Prime Factor of " + str(example) + " is: " + str(largestPrimeFactor(example)))
print("Test Completed")