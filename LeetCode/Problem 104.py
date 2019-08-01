# LeetCode: Problem 104
# Jonathan Kosasih

#Given a binary tree, find its maximum depth.
#
#The maximum depth is the number of nodes along the longest path
#from the root node down to the farthest leaf node.
#
#Note: A leaf is a node with no children.
#
#Example:
#Given binary tree [3,9,20,null,null,15,7],
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its depth = 3.
#------------------------------------------------------------------
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# at first it seems like DFS would be the obvious route to take, but since we need to check
# every node at least once anyways, we can do it with BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(not root):
            return 0
        queue = [root]
        depth = 0
        while(queue):
            levelResult = []
            newQueue = []
            for node in queue:
                if(node):
                    levelResult.append(node.val)
                    newQueue.append(node.left)
                    newQueue.append(node.right)
            queue = newQueue
            if(levelResult):
                depth += 1
        return depth
    
sol = Solution()
rootNode = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
rootNode.left = node1
rootNode.right = node2
node2.left = node3
node2.right = node4
print(str(sol.maxDepth(rootNode)))