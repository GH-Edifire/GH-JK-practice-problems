# LeetCode: Problem 21
# Jonathan Kosasih

#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
#Example:
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 is None):
            return l2
        elif(l2 is None):
            return l1
        
        if(l2.val > l1.val):
            newHead = ListNode(l1.val)
            l1 = l1.next
        else:
            newHead = ListNode(l2.val)
            l2 = l2.next
        pointer = newHead
        while(l1 is not None or l2 is not None):
            if(l1 is None):
                pointer.next = ListNode(l2.val)
                l2 = l2.next
                pointer = pointer.next
            elif(l2 is None or (l2.val > l1.val)):
                pointer.next = ListNode(l1.val)
                l1 = l1.next
                pointer = pointer.next
            else:
                pointer.next = ListNode(l2.val)
                l2 = l2.next
                pointer = pointer.next
        return newHead
        
    def printListNodes(self, head):
        while(head is not None):
            print(head.val, end = " ")
            head = head.next

sol = Solution()
example1 = ListNode(1)
example2 = ListNode(2)
example3 = ListNode(4)
example1.next = example2
example2.next = example3
sol.printListNodes(example1)
print("\n----------------------------")
example4 = ListNode(1)
example5 = ListNode(3)
example6 = ListNode(4)
example4.next = example5
example5.next = example6
sol.printListNodes(example4)
print("\n----------------------------")
newHead = sol.mergeTwoLists(example1,example4)
sol.printListNodes(newHead)