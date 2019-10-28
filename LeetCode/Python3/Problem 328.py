# LeetCode: Problem 328
# Jonathan Kosasih

#Given a singly linked list, group all odd nodes together followed by the even nodes.
#Please note here we are talking about the node number and not the value in the nodes.
#
#You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
#Example 1:
#Input: 1->2->3->4->5->NULL
#Output: 1->3->5->2->4->NULL
#
#Example 2:
#Input: 2->1->3->5->6->4->7->NULL
#Output: 2->3->6->7->1->5->4->NULL
#
#Note:
#The relative order inside both the even and odd groups should remain as it was in the input.
#The first node is considered odd, the second node even and so on ...
#------------------------------------------------------------------
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(not head):
            return head
        if(not head.next):
            return head
        count = 3
        odd = head
        evenStart = head.next
        even = head.next
        current = even.next
        while(current):
            if(count % 2 == 1):
                odd.next = current
                odd = current
            else:
                even.next = current
                even = current
            count += 1
            current = current.next
        even.next = None
        odd.next = evenStart
        return head
            
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
sol.oddEvenList(node1)
node = node1
while(node):
    print(str(node.val))
    node = node.next