# LeetCode: Problem 230
# Jonathan Kosasih

#Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
#Note:
#You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
#Example 1:
#Input: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#Output: 1
#
#Example 2:
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#Output: 3
#------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BST, travel in-order, add elements to array, sort, then just take the kth entry
    # slow, needs to travel the entire tree
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = []
        data = []
        node = root
        while(True):
            # reach the leftmost first
            if(node is not None):
                array.append(node)
                data.append(node.val)
                node = node.left
            # go right
            elif(array):
                node = array.pop()
                node = node.right
            else:
                break
        return sorted(data)[k-1]
    
    # OPTIMIZED in-order, much faster, stops at the kth element
    def kthSmallestAlt(self, root: TreeNode, k: int) -> int:
        array = []
        while(True):
            # add left first
            while(root):
                array.append(root)
                root = root.left
            # pop and go right
            root = array.pop()
            k -= 1
            if(k == 0):
                return root.val
            root = root.right
            
            
sol = Solution()
node5 = TreeNode(5)
node3 = TreeNode(3)
node6 = TreeNode(6)
node2 = TreeNode(2)
node4 = TreeNode(4)
node1 = TreeNode(1)
node5.left = node3
node5.right = node6
node3.left = node2
node3.right = node4
node2.left = node1
print(str(sol.kthSmallest(node5, 3)))