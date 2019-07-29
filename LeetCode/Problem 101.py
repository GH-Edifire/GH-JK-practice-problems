# LeetCode: Problem 101
# Jonathan Kosasih

#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
# 
#But the following [1,2,2,null,3,null,3] is not:
#
#    1
#   / \
#  2   2
#   \   \
#   3    3
#------------------------------------------------------------------
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return True
        if(not root.left and not root.right):
            return True
        if((root.left and not root.right) or (root.right and not root.left)):
            return False
        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while(queue):
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if(node1 is None and node2 is None):
                continue
            if((node1 and node2 is None) or (node2 and node1 is None) or (node1.val != node2.val)):
                return False
            
            queue.append(node1.left)
            queue.append(node2.right)
            
            queue.append(node2.left)
            queue.append(node1.right)
        return True
    
sol = Solution()
rootNode = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(3)
rootNode.left = node1
rootNode.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
print(str(sol.isSymmetric(rootNode)))