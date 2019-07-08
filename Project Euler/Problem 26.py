# Project Euler: Problem 26
# Jonathan Kosasih

#A unit fraction contains 1 in the numerator.
#The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#1/2 =   0.5
#1/3 =   0.(3)
#1/4 =   0.25
#1/5 =   0.2
#1/6 =   0.1(6)
#1/7 =   0.(142857)
#1/8 =   0.125
#1/9 =   0.(1)
#1/10    =   0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#------------------------------------------------------------------
def answer():
    # check for any cycles using remainders
    # with a remainder * 10, check again for remainder and repeat
    # if we encounter a remainder we have already seen, a new cycle is beginning
    # maximum recurring cycle will be length denominator - 1, so for largest cycle start at the highest index and work down
    cycleLength = 0
    for index in range(1000,1,-1):
        # cycle length is >= denominator, we must have found the max recurring cycle length
        if(cycleLength >= index):
            break
        remainders = [0 for i in range(index)]
        value = 1
        digitPosition = 0
        while(remainders[value] == 0 and value != 0):
            remainders[value] = digitPosition
            value *= 10
            value %= index
            digitPosition += 1
        if(digitPosition - remainders[value] > cycleLength):
            cycleLength = digitPosition - remainders[value]
    return cycleLength 

ans = answer()
print(str(ans))
