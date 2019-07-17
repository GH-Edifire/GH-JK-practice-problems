# Project Euler: Problem 33
# Jonathan Kosasih

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
#may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction, less than one in value
#and containing two digits in the numerator and denominator.
#
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#------------------------------------------------------------------
import fractions
def answer():
    ans = 1
    for i in range(10,100):
        for j in range(i+1,100):
            # check what digits are shared
            commonDigits = list(set(str(i)) & set(str(j)))
            if(len(commonDigits) != 0):
                # only check if common digits are not 0
                if(commonDigits[0] != "0"):
                    num = list(str(i))
                    den = list(str(j))
                    num.remove(commonDigits[0])
                    den.remove(commonDigits[0])
                    # check if remaining numbers are not 0
                    if(num[0] != "0" and den[0] != "0"):
                        if(fractions.Fraction(int(num[0]),int(den[0])) == fractions.Fraction(i,j)):
                            ans *= fractions.Fraction(i,j)
    return ans.denominator
        
ans = answer()
print(str(ans))
