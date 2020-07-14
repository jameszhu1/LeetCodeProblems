#finds if binary tree is balanced
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class BalancedSolution:
    def isBalanced(self, root):
        if root is None:
            return True
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if node is None:
            return 0
        lnode = self.getHeight(node.left)
        rnode = self.getHeight(node.right)
        if (lnode == -1) or (rnode == -1) or (abs(lnode - rnode) > 1):
            return -1

        return max(lnode, rnode) + 1

#Finds minimum depth of a tree
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class MinDepthSolution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

#Finds a path of a tree when adding all the nodes equals the target value
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif (not root.left) and (not root.right) and (sum - root.val == 0):
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
