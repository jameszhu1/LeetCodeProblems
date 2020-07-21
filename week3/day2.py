#contains duplicates leetcode 218
class ContainDuplicatesSolution:
    def containsDuplicate(self, nums):
        dup = {}
        for n in nums:
            if n not in dup:
                dup[n] = 1
            else:
                return True
        return False

#contains duplicates 2 leetcode 219
class ContainsDuplciates2Solution:
    def containsNearbyDuplicate(self, nums, k):
        dup = {}
        for i, n in enumerate(nums):
            if (n in dup) and (abs(i - dup[n]) <= k):
                    return True
            else:
                dup[n] = i
        return False

#invert a Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        #-----Recursive-------
        #if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        #-----Interative-------
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
