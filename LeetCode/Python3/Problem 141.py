# LeetCode: Problem 141
# Jonathan Kosasih

#Given a linked list, determine if it has a cycle in it.
#
#To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
#the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        scout = head
        while(scout):
            scout = scout.next
            if(not scout):
                return False
            else:
                scout = scout.next
            if(scout == current):
                return True
            current = current.next
        return False
        

sol = Solution()
node3 = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node4 = ListNode(-4)
node3.next = node2
node2.next = node0
node0.next = node4
node4.next = node2
print(str(sol.hasCycle(node3)))
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1
print(str(sol.hasCycle(node1)))
node1 = ListNode(1)
print(str(sol.hasCycle(node1)))