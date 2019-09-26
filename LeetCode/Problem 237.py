# LeetCode: Problem 237
# Jonathan Kosasih

#Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
sol = Solution()
node4 = ListNode(4)
node5 = ListNode(5)
node1 = ListNode(1)
node9 = ListNode(9)
node4.next = node5
node5.next = node1
node1.next = node9

node = node4

while(node):
    print(node.val)
    node = node.next
print()
    
sol.deleteNode(node5)
node = node4

while(node):
    print(node.val)
    node = node.next