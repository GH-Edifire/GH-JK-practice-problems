# Project Euler: Problem 41
# Jonathan Kosasih

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
#For example, 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?
#------------------------------------------------------------------
# max pandigital number will be 10 digits
# still leaves a lot of options so lets try the 3's division rule (number's sum of digits will be divisible by 3)
# 9+8+7+6+5+4+3+2+1+0 = 45, 45/3 = 15
# 9+8+7+6+5+4+3+2+1 = 45, 45/3 = 15
# 8+7+6+5+4+3+2+1 = 36, 36/3 = 12
# 7+6+5+4+3+2+1 = 28, 28/3 = 9.333…
# 6+5+4+3+2+1 = 21, 21/3 = 7
# 5+4+3+2+1 = 15, 15/3 = 5
# 4+3+2+1 = 10, 4/3 = 1.333…
# 3+2+1 = 6, 6/3 = 2
# 2+1 = 3 3/3 = 1
# 1 = 1/3 = .33

# 7, 4, and 1 digits work. We already know 1-digit is beaten by the prompt (4-digit) so ignore that
# check 7-digit values that are odd and work our way down

import eulerlib
def answer():
    ans = 7654321 # biggest pandigital 7-digit number
    while not (eulerlib.is_prime(ans) and isPandigital(ans,len(str(ans)))):
        ans -= 2
        if(ans < 1000000):
            ans = 4321
    
    return str(ans)

def isPandigital(number, length):
    tracker = [0] * 10
    for digit in str(number):
        if(int(digit) > int(length)):
            return False
        tracker[int(digit)] += 1
    for i in range(len(tracker)):
        if(tracker[i] > 1):
            return False
    return True
        
ans = answer()
print(str(ans))