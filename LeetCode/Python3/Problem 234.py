# LeetCode: Problem 234
# Jonathan Kosasih

#Given a singly linked list, determine if it is a palindrome.

#Example 1:
#Input: 1->2
#Output: false
#
#Example 2:
#Input: 1->2->2->1
#Output: true
#------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(n) time, O(n) space
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while(head):
            nodes.append(head.val)
            head = head.next
        return nodes == nodes[::-1]
    
    # O(n) time, O(1) space
    def isPalindromeAlt(self, head: ListNode) -> bool:
        slow = fast = head
        # find midpoint
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        node = None
        # found midpoint, now reverse the 2nd half
        while(slow):
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        # compare from beginning to reversed 2nd half
        while(node):
            if(node.val != head.val):
                return False
            node = node.next
            head = head.next
        return True
            
sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
print(str(sol.isPalindrome(node1)))
node1 = ListNode(-129)
node2 = ListNode(-129)
node1.next = node2
print(str(sol.isPalindrome(node1)))