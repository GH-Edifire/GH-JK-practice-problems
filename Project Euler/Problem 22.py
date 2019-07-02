# Project Euler: Problem 22
# Jonathan Kosasih

#Using names.txt (p22_names.txt), a 46K text file containing over five-thousand first names,
#begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN,
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
#What is the total of all the name scores in the file?
#------------------------------------------------------------------
def answer():
    with open("p22_names.txt") as file:
        textFile = file.read()
    textFile = textFile.replace("\"","")
    textFile = textFile.strip().split(",")
    textFile.sort()
    totalScore = 0
    for index in range(len(textFile)):
        #          += individual name score * place on sorted list
        totalScore += nameScore(textFile[index]) * (index + 1)
    return totalScore

def nameScore(name):
    letters = list(name)
    letters = [ord(char) - 64 for char in letters]
    return sum(letters)

correct = 871198282
ans = answer()
print("Expected answer is: " + str(correct))
print("Calculated answer is: " + str(ans))
print("Correct answer!") if(ans == correct) else print("Wrong answer!")
