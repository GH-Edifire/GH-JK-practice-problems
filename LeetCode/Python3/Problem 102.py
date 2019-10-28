# LeetCode: Problem 102
# Jonathan Kosasih

#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7

#return its level order traversal as:
#[
#  [3],
#  [9,20],
#  [15,7]
#]
#------------------------------------------------------------------
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        queue = [root]
        levelOrder = []
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
                levelOrder.append(levelResult)
        return levelOrder
    
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
print(str(sol.levelOrder(rootNode)))