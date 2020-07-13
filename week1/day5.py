#Binary tree bottom up level order
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BottomUpSolution:
    def levelOrderSolution(self, root):
        if not root:
            return
        bfs = []
        queue = [root]
        while len(queue) > 0:
            values = []
            for i in range(len(queue)):
                node = queue.pop(0)
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            bfs.append(values)
        return reversed(bfs)
#Convert sorted list to Binary search tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTSolution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
