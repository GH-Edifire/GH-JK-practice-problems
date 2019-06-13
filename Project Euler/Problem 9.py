# Project Euler: Problem 9
# Jonathan Kosasih

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#------------------------------------------------------------------
def answer():
    total = 1000
    for a in range(1, total + 1):
        for b in range(a+1, total + 1):
            c = total - a - b
            if(a*a + b*b == c*c):
                product = a*b*c
                return a,b,c, product

a,b,c,product = answer()
print(str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c))
print(str(a) + " * " + str(b) + " * " + str(c) + " = " + str(product))
print("Test complete")