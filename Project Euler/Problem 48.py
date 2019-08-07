# Project Euler: Problem 48
# Jonathan Kosasih

#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
#------------------------------------------------------------------
import math
def answer():
    ans = 0
    for i in range(1,1001):
        ans += i**i
    return str(ans)[-10:]
ans = answer()
print(str(ans))