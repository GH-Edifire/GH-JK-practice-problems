# Project Euler: Problem 40
# Jonathan Kosasih

#An irrational decimal fraction is created by concatenating the positive integers:
#
#0.123456789101112131415161718192021...
#
#It can be seen that the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#------------------------------------------------------------------
def answer():
    # the "0." part doesn't really matter, just ignore it
    s = "".join(str(i) for i in range(1, 1000000))
    ans = 1
    for i in range(7):
        ans *= int(s[10**i - 1])
    return str(ans)
        
ans = answer()
print(str(ans))