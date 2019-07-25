# Project Euler: Problem 39
# Jonathan Kosasih

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
#there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p ≤ 1000, is the number of solutions maximised?
#------------------------------------------------------------------
# p = a + b + c
# p = a + b + √(a^2+b^2)
# a = 0, p = 2a, a <= 500
# same with b
from collections import Counter
def answer():
    ans = 0
    solutions = []
    for a in range(1, 501):
        for b in range(a, 501):
            c = (a*a + b*b)**0.5
            if(int(c) == c and a + b + c <= 1000):
                solutions.append(a+b+c)
    count = Counter(solutions)
    ans,solNum = count.most_common(1)[0]
    return int(ans)
        
ans = answer()
print(str(ans))