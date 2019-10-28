# LeetCode: Problem 160
# Jonathan Kosasih

#Write a program to find the node at which the intersection of two singly linked lists begins.
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # O(3n) == O(n) runtime, O(1) space
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(not headA or not headB):
            return None
        # check if last node for both is the same, also counting lengths
        scoutA = headA
        lengthA = 0
        scoutB = headB
        lengthB = 0
        while(scoutA.next):
            scoutA = scoutA.next
            lengthA += 1
        while(scoutB.next):
            scoutB = scoutB.next
            lengthB += 1
        # if the last node is not the same, there is no intersection
        if(scoutA != scoutB):
            return None
        
        # last node is the same, so we look for the intersection
        scoutA = headA
        scoutB = headB
        # if the lengths differ, advance the longer one until they are the same length
        # just in case, keep checking for intersecting node
        if(lengthA > lengthB):
            i = 0
            while(i < (lengthA - lengthB)):
                scoutA = scoutA.next
                i += 1
                if(scoutA == scoutB):
                    return scoutA
        elif(lengthA < lengthB):
            i = 0
            while(i < (lengthB - lengthA)):
                scoutB = scoutB.next
                i += 1
                if(scoutA == scoutB):
                    return scoutA
        # same lengths, compare each node
        while(scoutA != scoutB):
            scoutA = scoutA.next
            scoutB = scoutB.next
            
        return scoutA
        
sol = Solution()
nodeA1 = ListNode(4)
nodeA2 = ListNode(1)
nodeB1 = ListNode(5)
nodeB2 = ListNode(0)
nodeB3 = ListNode(1)
nodeC1 = ListNode(8)
nodeC2 = ListNode(4)
nodeC3 = ListNode(5)

nodeA1.next = nodeA2
nodeA2.next = nodeC1
nodeC1.next = nodeC2
nodeC2.next = nodeC3
nodeB1.next = nodeB2
nodeB2.next = nodeB3
nodeB3.next = nodeC1

print(sol.getIntersectionNode(nodeA1, nodeB1).val)