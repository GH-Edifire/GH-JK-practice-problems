# LeetCode: Problem 103
# Jonathan Kosasih

#Given a binary tree, return the zigzag level order traversal of its nodes' values.
#(ie, from left to right, then right to left for the next level and alternate between).
#
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its zigzag level order traversal as:
#[
#  [3],
#  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return []
        goRight = True
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
            if(goRight):
                goRight = False
            else:
                # if not allowed to use reverse(), make function where you use another stack to reverse the current stack
                levelResult.reverse()
                goRight = True
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
print(str(sol.zigzagLevelOrder(rootNode)))