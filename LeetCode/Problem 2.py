# LeetCode: Problem 1
# Jonathan Kosasih

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # MAIN ANSWER
    #-----------------
    def addTwoNumbers(self, l1, l2, carry = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answerVal = l1.val + l2.val + carry
        carry = answerVal // 10
        answer = ListNode(answerVal % 10) 
        
        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            answer.next = self.addTwoNumbers(l1.next,l2.next,carry)
        return answer
    #-----------------
    
    # Print formattings
    def printInput(self, l1, l2):
        print("Input: (", end=" ")
        while (l1 != None):
            print(str(l1.val), end= " ")
            if(l1.next != None):
                print("->", end= " ")
                l1 = l1.next
            else:
                break
        print(") + (", end=" ")
        while (l2 != None):
            print(str(l2.val), end= " ")
            if(l2.next != None):
                print("->", end= " ")
                l2 = l2.next
            else:
                break
        print(")", end="\n")
    def printOutput(self, answer):
        print("Output: (", end=" ")
        while (answer != None):
            print(str(answer.val), end= " ")
            if(answer.next != None):
                print("->", end= " ")
                answer = answer.next
            else:
                break
        print(")", end="\n")
    def printAnswer(self, l1, l2, answer):
        print("Explanation: ", end=" ")
        firstNum = ""
        secondNum = ""
        answerNum = ""
        while (l1 != None):
            firstNum = str(l1.val) + firstNum
            if(l1.next != None):
                l1 = l1.next
            else:
                break
        print(firstNum + " +", end=" ")
        while (l2 != None):
            secondNum = str(l2.val) + secondNum
            if(l2.next != None):
                l2 = l2.next
            else:
                break
        print(secondNum + " =", end=" ")
        while (answer != None):
            answerNum = str(answer.val) + answerNum
            if(answer.next != None):
                answer = answer.next
            else:
                break
        print(answerNum, end="\n")
        
# test case
firstNumOne = ListNode(2)
firstNumTwo = ListNode(4)
firstNumThree = ListNode(3)
firstNumOne.next = firstNumTwo
firstNumTwo.next = firstNumThree

secondNumOne = ListNode(5)
secondNumTwo = ListNode(6)
secondNumThree = ListNode(4)
secondNumOne.next = secondNumTwo
secondNumTwo.next = secondNumThree
#-----------------
sol = Solution()
sol.printInput(firstNumOne,secondNumOne)
answer = sol.addTwoNumbers(firstNumOne,secondNumOne)
sol.printOutput(answer)
sol.printAnswer(firstNumOne,secondNumOne,answer)