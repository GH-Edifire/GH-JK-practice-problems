# Project Euler: Problem 42
# Jonathan Kosasih

#The nth term of the sequence of triangle numbers is given by,
#tn = ½n(n+1); so the first ten triangle numbers are:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#By converting each letter in a word to a number corresponding to its alphabetical position
#and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
#If the word value is a triangle number then we shall call the word a triangle word.
#
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
#two-thousand common English words, how many are triangle words?
#------------------------------------------------------------------
import itertools
def answer():
    file = open("p042_words.txt")
    data = file.readline()
    strings = data.split(",")
    total = 0
    for word in strings:
        if(isTriangleNumber(sum((ord(char) - ord('A') + 1) for char in word[1:len(word)-1]))):
            total +=1
    return total
        
def isTriangleNumber(num):
    triangle = 0
    for i in itertools.count():
        triangle += i
        if(num == triangle):
            return True
        elif(num < triangle):
            return False
        
ans = answer()
print(str(ans))