# LeetCode: Problem 94
# Jonathan Kosasih

#Given a binary tree, return the inorder traversal of its nodes' values.
#
#Example:
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
#Output: [1,3,2]
#Follow up: Recursive solution is trivial, could you do it iteratively?
#------------------------------------------------------------------
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # recursive solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(not root):
            return []
        ans = []
        self.inorderHelper(root,ans)
        return ans
    
    def inorderHelper(self, root, returnList):
        if(root.left):
            self.inorderHelper(root.left, returnList)
        returnList.append(root.val)
        if(root.right):
            self.inorderHelper(root.right, returnList)
    
    # iterative
    def inorderTraversalIterative(self, root):
        if(not root):
            return []
        ans = []
        stack = []
        while(stack or root):
            if(root):
                stack.append(root)
                root = root.left
            else:
                tempNode = stack.pop()
                ans.append(tempNode.val)
                root = tempNode.right
        return ans
        
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3
sol = Solution()
print(str(sol.inorderTraversal(node1)))
print(str(sol.inorderTraversalIterative(node1)))
node1 = None
print(str(sol.inorderTraversal(node1)))
print(str(sol.inorderTraversalIterative(node1)))