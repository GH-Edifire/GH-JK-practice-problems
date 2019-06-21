# Project Euler: Problem 15
# Jonathan Kosasih

#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#
#How many such routes are there through a 20×20 grid?
#------------------------------------------------------------------
# 2x2
# rrdd, rdrd, rddr, drrd, drdr, ddrr
# amount of rights must match amount of downs
# rights + downs = 2n
# basically comes down to 2n choose n (2n choices, choose n to form a path, grab all unique paths)
import math
def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
n = 40
r = 20
print(str(nCr(n,r)))
print("Test complete")