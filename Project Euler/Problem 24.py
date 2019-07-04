# Project Euler: Problem 24
# Jonathan Kosasih

#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#------------------------------------------------------------------
import itertools
def answer():
    # range is 0-9
    arr = list(range(10))
    # retrieve the 999,999th permutation (0 based indexing == 1,000,000)
    temp = itertools.islice(itertools.permutations(arr), 999999, None)
    # convert to string
    return "".join(str(x) for x in next(temp))

ans = answer()
print(str(ans))
