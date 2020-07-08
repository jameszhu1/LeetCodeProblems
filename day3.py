#Given 2 binary strings, return their sum (in binary)
class BinarySolution:
    def addBinary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == "1" and b[-1] == "1":
            print("1st if", self.addBinary(self.addBinary(a[0:-1], b[0:-1]), "1") + "0")
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), "1") + "0"
        if a[-1] == "0" and b[-1] == "0":
            print("3rd if", self.addBinary(a[0:-1], b[0:-1]) + "0")
            return self.addBinary(a[0:-1], b[0:-1]) + "0"
        else:
            print("4th if", self.addBinary(a[0:-1], b[0:-1]) + "1")
            return self.addBinary(a[0:-1], b[0:-1]) + "1"
q1 = BinarySolution()
print(q1.addBinary("1010", "1011"))
#how many different ways can you climb n stairs if you can only take 1 or 2 steps.
class StairsSolution:
    def climbStairs(self, n):
        '''if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)'''
    #Dynamic programming Bottom-up
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        addDict = {1: 1, 2: 2}
        for i in range(3, n + 1):
            currentVal = addDict[i - 1] + addDict[i - 2]
            addDict[i] = currentVal
        return addDict[n]
q2 = StairsSolution()
print(q2.climbStairs(6))
#Remove duplicated nodes in sorted LL
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class RemoveDupLLSolution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
#Merge both with O(m+n) space
class mergeSolution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m - 1 + n] = nums2[n - 1]
                n = n - 1
            else:
                nums1[m - 1 + n], nums1[m - 1] = nums1[m - 1], nums1[m - 1 + n]
                m = m - 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]

q4 = mergeSolution()
n1 = [1,2,3,0,0,0]
n2 = [2,5,6]
q4.mergeSortedArray(n1, 3, n2, 3)
print(n1)
