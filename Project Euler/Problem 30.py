# Project Euler: Problem 30
# Jonathan Kosasih

#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#1634 = 1^4 + 6^4 + 3^4 + 4^4
#8208 = 8^4 + 2^4 + 0^4 + 8^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 1^4 is not a sum it is not included.
#
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#------------------------------------------------------------------
# real problem is determining the upper bound
# highest digit is 9, power we are looking for is the 5th power so 9^5 = 59049
# 59049 has 5 digits, so lets try 5 * 9^5 = 295245
# 295245 has 6 digits, so try 6 * 9^5 = 354294, also 6 digits
# just make 355000 our upper bound
# OR also upper bound = (exponent + 1) * 9^exponent

powers = {}
for digit in range(10):
    powers[digit] = digit ** 5
    
def answer():
    # skip 1
    total = 0
    for index in range(2,355000):
        if(index == fifthPowerSum(index)):
            total += index
    return total
def fifthPowerSum(number):
    total = 0
    for digit in str(number):
        total += powers[int(digit)]
    return total
ans = answer()
print(str(ans))
