# LeetCode: Problem 105
# Jonathan Kosasih

#Given preorder and inorder traversal of a tree, construct the binary tree.
#
#Note:
#You may assume that duplicates do not exist in the tree.
#
#For example, given
#
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]
#Return the following binary tree:
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#------------------------------------------------------------------
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if(not preorder or not inorder):
            return None
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        inorderIndex = inorder.index(rootVal)
        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex+1:])
        return root
        
    
#sol = Solution()
#rootNode = TreeNode(3)
#node1 = TreeNode(9)
#node2 = TreeNode(20)
#node3 = TreeNode(15)
#node4 = TreeNode(7)
#rootNode.left = node1
#rootNode.right = node2
#node2.left = node3
#node2.right = node4
#print(str(sol.maxDepth(rootNode)))