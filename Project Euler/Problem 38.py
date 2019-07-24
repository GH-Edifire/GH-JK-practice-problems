# Project Euler: Problem 38
# Jonathan Kosasih

#Take the number 192 and multiply it by each of 1, 2, and 3:
#
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576.
#We will call 192384576 the concatenated product of 192 and (1,2,3)
#
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
#giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as
#the concatenated product of an integer with (1,2, ... , n) where n > 1?
#------------------------------------------------------------------
# we know that the number must be >= 918273645 from the prompt, and initial number cant be 9
# initial number will probably be 4 digits, since 4 digits * 1 == 4 digits, 4 digits * 2 == 4 or 5 digits
# (5 or more digits * 2 will give at least 10 concatenated digits)
# therefore, limit is 10,000
# work our way down from there
def answer():
    ans = ""
    for i in range(9999, -1,-1):
        # at max, the check runs 9 times (1 digit * 9), but we will find the answer before getting that far down
        temp = str(i)
        for j in range(2,10):
            temp = temp + str(i*j)
            if(len(str(temp)) == 9):
                if("".join(sorted(temp)) == "123456789"):
                    ans = max(ans, temp)
            if(len(str(temp)) > 9):
                break
    return ans
        
ans = answer()
print(str(ans))