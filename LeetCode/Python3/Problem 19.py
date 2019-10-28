# LeetCode: Problem 19
# Jonathan Kosasih

#Given a linked list, remove the n-th node from the end of list and return its head.
#
#Example:
#
#Given linked list: 1->2->3->4->5, and n = 2.
#
#After removing the second node from the end, the linked list becomes 1->2->3->5.
#Note:
#
#Given n will always be valid.
#------------------------------------------------------------------
 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        scoutPointer = head
        mainPointer = head
        index = 0
        while(scoutPointer.next is not None):
            if(index >= n):
                mainPointer = mainPointer.next
            scoutPointer = scoutPointer.next
            index += 1
        if(n == index+1):
            head = head.next
        else:
            mainPointer.next = mainPointer.next.next
        return head
    
    # slightly faster but same concept
    def removeNthFromEndAlt(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
    
    def printLinkedList(self, head):
        while(head is not None):
            print(str(head.val))
            head = head.next
        
        
sol = Solution()
example1 = ListNode(1)
example2 = ListNode(2)
example3 = ListNode(3)
example4 = ListNode(4)
example5 = ListNode(5)
example1.next = example2
example2.next = example3
example3.next = example4
example4.next = example5
sol.printLinkedList(example1)
print("------------------------------")
sol.printLinkedList(sol.removeNthFromEnd(example1,2))
