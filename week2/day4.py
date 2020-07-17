#Given a non-empty array of integers, every element appears twice except for one, find it. leetcode 136
class Solution:
    def singleNumber(self, nums):
        numCount = {}
        for n in nums:
            if n in numCount:
                numCount[n] += 1
            else:
                numCount[n] = 1
        for key, val in numCount.items():
            if val < 2:

                return key
#stack operations
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        if not self.stack:
            self.stack.append([x,x])
        else:
            self.stack.append([x, min(x, self.stack[-1][1])])
    def pop(self):
        if self.stack:
            self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]

#detect linked list cycle leetcode 141
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slowPointer = head
        fastPointer = head
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                return True
        return False
