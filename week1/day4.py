#Checks if both trees are the same
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SameTreeSolution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        if p.val != q.val:
            return False
        leftSubTree = self.isSameTree(p.left, q.left)
        rightSubTree = self.isSameTree(p.right, q.right)
        return leftSubTree and rightSubTree
#Checks if a tree is mirrored
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class symmetrySolution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSame(root.left, root.right)

    def isSame(self, l, r):
        if l and r:
            return l.val == r.val and self.isSame(l.right, r.left) and self.isSame(l.left, r.right)
        else:
            return l is r
#Checks depth of tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class maxDepthSolution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1
