# LeetCode: Problem 236
# Jonathan Kosasih

#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
#According to the definition of LCA on Wikipedia:
#“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both
#p and q as descendants (where we allow a node to be a descendant of itself).”
#
#Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS recursion
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(currentNode):
            if(not currentNode):
                return False
            # check left side
            left = recurse(currentNode.left)
            # check right side
            right = recurse(currentNode.right)
            # check if current is p or q
            mid = currentNode == p or currentNode == q
            # found at least 2, save lowest ancestor
            if(mid + left + right >= 2):
                self.ans = currentNode
            return mid or left or right
        recurse(root)
        return self.ans
            
sol = Solution()
node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node7 = TreeNode(7)
node4 = TreeNode(4)
node0 = TreeNode(0)
node8 = TreeNode(8)
node3.left = node5
node3.right = node1
node1.left = node0
node1.right = node8
node5.left = node6
node5.right = node2
node2.left = node7
node2.right = node4
print(str(sol.lowestCommonAncestor(node3, node5, node4).val))
