# LeetCode: Problem 206
# Jonathan Kosasih

#Reverse a singly linked list.
#
#Example:
#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # initial solution, iterative
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head):
            return None
        scout = head
        current = None
        while(scout):
            temp = scout.next
            scout.next = current
            current = scout
            scout = temp
        return current
    
    # recursive solution
    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        # travel all the way to the end, then start setting stuff
        temp = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return temp
    
    def display(self, head):
        while(head):
            print(str(head.val))
            head = head.next

sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
sol.display(node1)
print("------")
sol.display(sol.reverseList(node1))
#sol.display(sol.reverseListRecursive(node1))
