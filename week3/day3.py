#lowest common ancestor of a binary search tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LCASolution:
    def lowestCommonAncestor(self, root, p, q):
        #RECURSIVE WAY
        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root

        while True:
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                return root
            elif p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
#delete a node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DeleteNodeSolution:
    def deleteNode(self, node):
        if node.next is not None:
            node.val = node.next.val
            node.next = node.next.next
#valid anagram
class AnagramSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in t:
            if j not in d:
                return False
            else:
                d[j] -= 1
        for val in d.values():
            if val != 0:
                return False
        return True
