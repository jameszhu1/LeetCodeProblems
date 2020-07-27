# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class BadVersionSolution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

#list of all paths of a tree
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class TreePathsSolution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = []
        self.dfs(root, "", paths)
        return paths

    def dfs(self, root, strPointer, paths):
        if not root.left and not root.right:
            paths.append(strPointer + str(root.val))
        if root.left:
            self.dfs(root.left, strPointer + str(root.val) + "->", paths)
        if root.right:
            self.dfs(root.right, strPointer + str(root.val) + "->", paths)

#find digital root
class DigitalRootSolution:
    def addDigits(self, num):
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

#find missing num from list
class MissingNumSolution:
    def missingNumber(self, nums):
        #gauss formula to get the sum of the first n numbers
        gauss_sum = len(nums)*(len(nums) + 1) // 2
        nums_sum = sum(nums)
        return gauss_sum - nums_sum
