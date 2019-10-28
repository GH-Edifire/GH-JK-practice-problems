# LeetCode: Problem 138
# Jonathan Kosasih

#A linked list is given such that each node contains an additional random pointer which could point to any node in the list
#or null.
#
#Return a deep copy of the list.
#------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dict = dict()
        m = n = head
        while m:
            dict[m] = Node(m.val, None, None)
            m = m.next
        while n:
            dict[n].next = dict.get(n.next)
            dict[n].random = dict.get(n.random)
            n = n.next
        return dict.get(head)

#sol = Solution()
#example = [2,2,1]
#print(str(sol.singleNumber(example)))