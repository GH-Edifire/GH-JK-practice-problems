# Project Euler: Problem 32
# Jonathan Kosasih

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
#for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
#and product is 1 through 9 pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#------------------------------------------------------------------
def answer():
    # avoid duplicates
    products = set()
    
    check = set('123456789')
    
    # len(a) + len(b) + len(a*b) = 9
    # len(a) = 1, len(b) must = 4, len(a*b) = 4
    # len(a) = 2, len(b) must = 3, len(a*b) = 4
    
    # --- pattern repeated below, therefore checking is unneeded
    # len(a) = 3, len(b) must = 2, len(a*b) = 4
    # len(a) = 4, len(b) must = 1, len(a*b) = 4
    
    #for single digit multiplicand
    for i in range(9):
        for j in range(999,9999):
            s = str(i)+str(j)+str(i*j)
            if(len(s) == 9 and set(s) == check):
                products.add(i*j)
            elif(len(s) > 9):break

    #for double digit multiplicand
    for i in range(9,99):
        for j in range(99,999):
            s = str(i)+str(j)+str(i*j)
            if(len(s) == 9 and set(s) == check):
                products.add(i*j)
            elif(len(s) > 9): break
            
    return sum(products)
        
ans = answer()
print(str(ans))
