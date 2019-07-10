# Project Euler: Problem 28
# Jonathan Kosasih

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#
#It can be verified that the sum of the numbers on the diagonals is 101.
#
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#------------------------------------------------------------------
# we can see a pattern, only adding odd numbers:
# skipping [] numbers
# adding 1, 3, 5, 7, 9,[11], 13, [15], 17,[19], 21,[23], 25,[27],[29], 31,[33][35] 37, [39][41] 43,[45][47] 49
#    gap    1  1  1  1       2         2        2        2             3           3            3           3
# gap between numbers increases by 2 every 4 iterations
def answer():
    lastNumber = 1001*1001
    oddNumbers = range(1, lastNumber+1, 2)
    index = 0
    gap = 1
    ans = 1
    while(oddNumbers[index] != lastNumber):
        for x in range(4):
            index += gap
            ans += oddNumbers[index]
        gap += 1
    return ans
ans = answer()
print(str(ans))
