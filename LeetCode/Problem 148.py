# LeetCode: Problem 148
# Jonathan Kosasih

#Sort a linked list in O(n log n) time using constant space complexity.
#
#Example 1:
#Input: 4->2->1->3
#Output: 1->2->3->4
#
#Example 2:
#Input: -1->5->3->4->0
#Output: -1->0->3->4->5
#------------------------------------------------------------------

# INITIAL THOUGHTS:
# This problem is difficult because of the constant space requirement
# can't load everything to an array, sort it, then reorganize data (O(n) space)
# can't use quicksort, mergesort, or any recursion based sorting (O(n) or more space because of recursion)
# can't bruteforce it because while it can meet the space requirement, it would be O(n^2) time
#
# FOR STUDYING:
# I am ashamed to say I had to look up a suitable answer.
# Apparently the traditional recursion mergesort is bad, but you can adapt it have no recursion
# Answered by simkieu:
# https://leetcode.com/problems/sort-list/discuss/46776/Python-O(nlogn)-time-O(1)-space-solution-with-explanation
# constant space, no arrays based on list length or recursion
# step size k is doubled each time, == log n
# done n number of times
# time complexity = O(nlogn)
# space complexity = O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Get head and tail of list1 and list 2 with k elements
    # If there is not enough elements, we just cut there and
    # leave them NULL
    def getHeads(self, head, k):
        h1, t1, h2, t2, nextHead = head, None, None, None, None
        t = h1
        count = 1
        while t and t.next and count < k:
            count += 1
            t = t.next
        t1 = t
        if t1:
            h2 = t.next
            t = t.next
        count += 1
        while t and t.next and count < 2*k:
            count += 1
            t = t.next
        t2 = t
        if t2:
            nextHead = t.next
        return h1, t1, h2, t2, nextHead
    
    # Merge 2 sorted LinkedLists and return their merged list's head and tail
    def merge(self, h1, t1, h2, t2):
        fakeHead = ListNode(0)
        t = fakeHead
        while h1 and h2:
            if h1.val <= h2.val:
                t.next = h1
                h1 = h1.next
            else:
                t.next = h2
                h2 = h2.next
            t = t.next
        if h1:
            t.next = h1
            newTail = t1
        else:
            t.next = h2
            newTail = t2
        return fakeHead.next, newTail
        
    def sortList(self, head):
        fakeHead = ListNode(0)
        fakeHead.next = head
        tmp = fakeHead
        k = 1
        h1, t1, h2, t2, nextHead = self.getHeads(head, k)
        while h2:
            tmp = fakeHead
            while h2:
                if t1: t1.next = None
                if t2: t2.next = None
                mergeHead, mergeTail = self.merge(h1, t1, h2, t2)
                tmp.next = mergeHead
                tmp = mergeTail
                h1, t1, h2, t2, nextHead = self.getHeads(nextHead, k)
            tmp.next = h1
            k *= 2
            h1, t1, h2, t2, nextHead = self.getHeads(fakeHead.next, k)
        return fakeHead.next
        
sol = Solution()
node4 = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)
node4.next = node2
node2.next = node1
node1.next = node3
head = sol.sortList(node4)
while(head):
    print(str(head.val))
    head = head.next