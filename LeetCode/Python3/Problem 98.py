# LeetCode: Problem 98
# Jonathan Kosasih

#Given a binary tree, determine if it is a valid binary search tree (BST).
#
#Assume a BST is defined as follows:
#
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.
#
#Example 1:
#    2
#   / \
#  1   3
#
#Input: [2,1,3]
#Output: true
#
#Example 2:
#    5
#   / \
#  1   4
#     / \
#    3   6
#
#Input: [5,1,4,null,null,3,6]
#Output: false
#Explanation: The root node's value is 5 but its right child's value is 4.
#------------------------------------------------------------------
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return (self.isValidBST(root.left, min(lessThan, root.val), largerThan) and 
               self.isValidBST(root.right, lessThan, max(root.val, largerThan)))
    
    # iteratively, in-order traversal
    # O(n) time and O(n)+O(lgn) space
    def isValidBST(self, root):
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            # if root is None or all the nodes have 
            # been traversed and have no confliction 
            if not stack:
                return True
            node = stack.pop()
            # res stores the current values in in-order 
            # traversal order, node.val should larger than
            # the last element in res
            if res and node.val <= res[-1]:
                return False
            res.append(node.val)
            root = node.right
    
    
root = TreeNode(5)
node1 = TreeNode(1)
node4 = TreeNode(4)
node3 = TreeNode(3)
node6 = TreeNode(6)
root.left = node1
root.right = node4
node4.left = node3
node4.right = node6
sol = Solution()
print(str(sol.isValidBST(root)))
root = TreeNode(2)
node1 = TreeNode(1)
node3 = TreeNode(3)
root.left = node1
root.right = node3
print(str(sol.isValidBST(root)))
root = TreeNode(1)
node1 = TreeNode(1)
root.left = node1
print(str(sol.isValidBST(root)))