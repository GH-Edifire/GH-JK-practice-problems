# Project Euler: Problem 43
# Jonathan Kosasih

#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
#but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.
#------------------------------------------------------------------
# could brute force this for 10-digit pandigital numbers, check every permutation for satisfying properties
# or can make some observations based on the given rules that will be done here:
#
# d4d5d6 is divisible by 5 means d6 must be 0 or 5
# d6d7d8 is divisible by 11, and d6 cannot be 0 because that will lead to non-unique combinations (011,022,...),
# d6 = 5
# subset d6d7d8 is limited to the 500's then, {506, 517, 528, 539, 561, 572, 583, 594}
# d7d8d9 is divisible by 13, which gives us 8 possible combination from above + another digit that is unique
# {065, 286, 390, 611, 728, 832, 949}
# using d6d7d8d9, and eliminating repeating digits, we have {5286, 5390, 5728, 5832}
# repeating the process for d8d9d10, and combining to d6d7d8d9d10 now we have {52867, 53901, 57289}
# d5d6d7 is divisible by 7 so we are more limited to {952867, 357289}
# d2d3d4 is divisible by 2, so d4 is even, {0952867, 4952867, 0357289, 4357289, 6357289} excluding repeating digits
# d3d4d5 is divisible by 3, and the numbers 2, 5, 7, 8, have confirmed places in the possible sets so d5 must end in
# 3 or 9
# {30952867, 60357289, 06357289}
# only numbers left are 1 and 4 for digits d1 and d2, therefore we have 6 numbers
# {1430952867, 1460357289, 1406357289, 4130952867, 4160357289, 4106357289}
def answer():
    possible = [1430952867, 1460357289, 1406357289, 4130952867, 4160357289, 4106357289]
    ans = sum(i for i in possible)
    return ans
        
ans = answer()
print(str(ans))