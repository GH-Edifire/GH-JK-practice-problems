# Project Euler: Problem 17
# Jonathan Kosasih
#
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
#The use of "and" when writing out numbers is in compliance with British usage.
#------------------------------------------------------------------
SINGLE_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def answer():
    return sum(len(translate(i)) for i in range(1,1001))

def translate(number):
    if(0 <= number < 20):
        return SINGLE_WORDS[number]
    elif(20 <= number < 100):
        return TENS[number//10] + (SINGLE_WORDS[number%10] if(number%10 != 0) else "")
    elif(100 <= number < 1000):
        return SINGLE_WORDS[number//100] + "hundred" + (("and" + translate(number%100)) if(number%100 != 0) else "")
    elif(1000 <= number < 1000000):
        return translate(number//1000) + "thousand" + (translate(number%1000) if(number%1000 != 0) else "")
    
print(str(answer()))
print("Test complete")